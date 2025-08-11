 American Sign Language (ASL) Detection
## Overview
This project builds a deep learning model to detect and classify American Sign Language (ASL) hand gestures into 29 classes — the English alphabet A–Z, along with three special signs: SPACE, DELETE, and NOTHING. The model uses Convolutional Neural Networks (CNNs) to process images and identify the correct sign.

## Objective
To create an accurate ASL detection system that:

Accepts an image of a hand sign as input.

Predicts the corresponding alphabet or action.

Supports 29 different classes.

## Dataset
Source: ASL Alphabet Dataset – Kaggle

Train Set: Contains separate folders for each class (A–Z, SPACE, DELETE, NOTHING).

Test Set: Contains sample test images for each class.

Total Classes: 29.

Example Folder Structure:

dataset/
│
├── train/
│   ├── A/
│   ├── B/
│   ├── ...
│   ├── SPACE/
│   ├── DELETE/
│   └── NOTHING/
│
└── test/
    ├── A_test.jpg
    ├── ...
## Technologies Used:
Python

TensorFlow / Keras

OpenCV (optional, for image processing)

NumPy, Pandas

Matplotlib, Seaborn (visualization)

Scikit-learn (metrics)

## Steps Followed
Data Loading & Preprocessing

Resizing images to 64x64.

Normalizing pixel values (0–1 range).

Data augmentation for better generalization.

Model Building

CNN architecture with Conv2D, MaxPooling, Flatten, and Dense layers.

Softmax activation for multi-class classification.

Training & Validation

Trained with categorical cross-entropy loss.

Monitored accuracy and loss on validation set.

Evaluation

Achieved high accuracy across all 29 classes.

Tested with unseen data for real-world validation.

Model Saving

Saved as .h5 file for later predictions.

## Results
Accuracy: ~95%+ on validation set (varies with hyperparameters).

Model generalizes well to unseen test images.

##How to Run
Clone the repository:


git clone <your-repo-link>
cd asl-detection
Install dependencies:

pip install -r requirements.txt
Download dataset - 
https://www.kaggle.com/datasets/grassknoted/asl-alphabet
from Kaggle and place it inside dataset/ folder.

Train the model:

python train.py
Run predictions:

python predict.py --image path/to/image.jpg
## Future Improvements
Integrate real-time webcam detection.

Build a Streamlit web app for interactive ASL translation.

Extend dataset with more lighting and background variations.

