# Emotion Sentiment Analysis

## Overview
This project implements a sentiment analysis model for text data using TensorFlow. It processes text inputs, classifies them into three sentiment categories (Positive, Negative, Neutral), and provides predictions based on the input text. The project includes data preprocessing, model training, evaluation, and deployment steps.

## Features
- Sentiment classification (Positive, Negative, Neutral)
- Text preprocessing with tokenization and padding
- Model training with TensorFlow
- Custom callback for early stopping at target accuracy
- Visualization of training and validation performance
- Exporting the model in TensorFlow Lite (TFLite) format for deployment

## Prerequisites
Before starting, ensure you have the following installed:
- Python 3.8 or later
- TensorFlow 2.x
- pandas
- matplotlib
- textblob
- scikit-learn

You can install the required libraries using:
```bash
pip install tensorflow pandas matplotlib textblob scikit-learn
```

## Dataset
The project uses a dataset containing text samples and corresponding emotion labels. The dataset should be provided as a CSV file with at least the following columns:
- `text`: The input text data.
- `Emotion`: The emotion label (used for filling missing values).

## Setup
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. Place your dataset in the root directory and ensure it is named `emotion_sentimen_dataset.csv`.

3. Run the script to preprocess data, train the model, and save outputs:
   ```bash
   python main.py
   ```

## Project Structure
```
.
├── Journal.py                 # Main script for training and evaluation
├── emotion_sentimen_dataset.csv  # Dataset file (not included in the repository)
├── model.keras             # Trained TensorFlow model
├── emotion_model.tflite    # TFLite model for deployment
├── README.md               # Journal ML documentation
```

## Usage
### Training the Model
The script processes the dataset, trains a sentiment analysis model, and saves the trained model in both `.keras` and `.tflite` formats. To train and evaluate the model:
```bash
python main.py
```

### Testing Predictions
After training, the script demonstrates predictions for sample inputs. You can modify `test_texts` in the script to test your custom inputs.

### Deploying the Model
Use the `emotion_model.tflite` file for deployment on edge devices or mobile applications.

## Results
The model achieves high accuracy for sentiment classification. The training and validation performance are visualized in accuracy and loss graphs.
