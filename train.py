import numpy as np
import matplotlib.pyplot as plt
from data_preprocessing import ASLDataPreprocessor
from model import ASLModel
import os

def plot_training_history(history):
    """Plot training history"""
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    
    # Plot accuracy
    axes[0].plot(history.history['accuracy'], label='Training Accuracy')
    axes[0].plot(history.history['val_accuracy'], label='Validation Accuracy')
    axes[0].set_title('Model Accuracy')
    axes[0].set_xlabel('Epoch')
    axes[0].set_ylabel('Accuracy')
    axes[0].legend()
    
    # Plot loss
    axes[1].plot(history.history['loss'], label='Training Loss')
    axes[1].plot(history.history['val_loss'], label='Validation Loss')
    axes[1].set_title('Model Loss')
    axes[1].set_xlabel('Epoch')
    axes[1].set_ylabel('Loss')
    axes[1].legend()
    
    plt.tight_layout()
    plt.savefig('results/training_history.png')
    plt.show()

def main():
    # Paths
    train_path = 'data/asl_alphabet_train'
    test_path = 'data/asl_alphabet_test'
    
    # Create directories
    os.makedirs('models', exist_ok=True)
    os.makedirs('results', exist_ok=True)
    
    # Initialize preprocessor
    preprocessor = ASLDataPreprocessor(train_path, test_path, img_size=(64, 64))
    
    # Explore dataset
    print("Exploring dataset...")
    class_counts = preprocessor.explore_dataset()
    preprocessor.visualize_samples(num_samples=3)
    
    # Load and preprocess data
    print("Loading and preprocessing data...")
    X_train, y_train_cat, y_train = preprocessor.load_and_preprocess_data()
    
    # Create train-validation split
    X_train_split, X_val, y_train_split, y_val = preprocessor.create_validation_split(
        X_train, y_train_cat
    )
    
    print(f"Training set: {X_train_split.shape}")
    print(f"Validation set: {X_val.shape}")
    
    # Create model
    model_builder = ASLModel(
        input_shape=(64, 64, 3),
        num_classes=len(preprocessor.classes)
    )
    
    # Option 1: CNN from scratch
    model = model_builder.create_cnn_model()
    
    # Option 2: Transfer learning (uncomment to use)
    # model = model_builder.create_transfer_learning_model()
    
    model_builder.compile_model(learning_rate=0.001)
    
    print(model.summary())
    
    # Get callbacks
    callbacks = model_builder.get_callbacks()
    
    # Train model
    print("Starting training...")
    history = model.fit(
        X_train_split, y_train_split,
        validation_data=(X_val, y_val),
        epochs=50,
        batch_size=32,
        callbacks=callbacks,
        verbose=1
    )
    
    # Plot training history
    plot_training_history(history)
    
    print("Training completed!")
    print(f"Best validation accuracy: {max(history.history['val_accuracy']):.4f}")

if __name__ == "__main__":
    main()