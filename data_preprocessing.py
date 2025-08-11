import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
import seaborn as sns

class ASLDataPreprocessor:
    def __init__(self, train_path, test_path, img_size=(64, 64)):
        self.train_path = train_path
        self.test_path = test_path
        self.img_size = img_size
        self.classes = []
        self.class_to_label = {}
        self.label_to_class = {}
        
    def explore_dataset(self):
        """Explore the dataset structure and visualize sample images"""
        # Get class names
        self.classes = sorted(os.listdir(self.train_path))
        print(f"Number of classes: {len(self.classes)}")
        print(f"Classes: {self.classes}")
        
        # Create label mappings
        self.class_to_label = {cls: idx for idx, cls in enumerate(self.classes)}
        self.label_to_class = {idx: cls for idx, cls in enumerate(self.classes)}
        
        # Count images per class
        class_counts = {}
        for class_name in self.classes:
            class_path = os.path.join(self.train_path, class_name)
            count = len(os.listdir(class_path))
            class_counts[class_name] = count
            
        # Visualize class distribution
        plt.figure(figsize=(15, 8))
        plt.bar(class_counts.keys(), class_counts.values())
        plt.title('Distribution of Images per Class')
        plt.xlabel('Classes')
        plt.ylabel('Number of Images')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
        return class_counts
    
    def visualize_samples(self, num_samples=5):
        """Visualize sample images from each class"""
        fig, axes = plt.subplots(len(self.classes), num_samples, 
                                figsize=(num_samples*2, len(self.classes)*2))
        
        for i, class_name in enumerate(self.classes):
            class_path = os.path.join(self.train_path, class_name)
            images = os.listdir(class_path)[:num_samples]
            
            for j, img_name in enumerate(images):
                img_path = os.path.join(class_path, img_name)
                img = cv2.imread(img_path)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                
                axes[i, j].imshow(img)
                axes[i, j].set_title(f'{class_name}')
                axes[i, j].axis('off')
                
        plt.tight_layout()
        plt.show()
    
    def load_and_preprocess_data(self):
        """Load and preprocess the training data"""
        X_train = []
        y_train = []
        
        print("Loading training data...")
        for class_name in self.classes:
            class_path = os.path.join(self.train_path, class_name)
            label = self.class_to_label[class_name]
            
            for img_name in os.listdir(class_path):
                try:
                    img_path = os.path.join(class_path, img_name)
                    img = cv2.imread(img_path)
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    img = cv2.resize(img, self.img_size)
                    img = img.astype('float32') / 255.0  # Normalize
                    
                    X_train.append(img)
                    y_train.append(label)
                except Exception as e:
                    print(f"Error processing {img_path}: {e}")
        
        X_train = np.array(X_train)
        y_train = np.array(y_train)
        
        # Convert labels to categorical
        y_train_categorical = to_categorical(y_train, num_classes=len(self.classes))
        
        print(f"Training data shape: {X_train.shape}")
        print(f"Training labels shape: {y_train_categorical.shape}")
        
        return X_train, y_train_categorical, y_train
    
    def create_validation_split(self, X_train, y_train, test_size=0.2):
        """Split training data into train and validation sets"""
        X_train_split, X_val, y_train_split, y_val = train_test_split(
            X_train, y_train, test_size=test_size, random_state=42, stratify=y_train
        )
        return X_train_split, X_val, y_train_split, y_val