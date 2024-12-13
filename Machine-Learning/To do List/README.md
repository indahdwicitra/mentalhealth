# To do List Recomendation Model #

## Description ## 
This machine learning model is a collaborative filtering-based recommendation system that uses embedding to learn the relationship between user professions and activities. The model predicts relevant activities based on the interaction patterns of professions and activity descriptions. The project was developed using TensorFlow and scikit-learn, with the final output being an .h5 file submitted to the cloud computing team for API integration

## Dataset ##
The dataset used is `updated_activities_dataset.csv` with main columns:
- `Profession` - User profession.
- `Activity Description` - Description of available activities.
- `Hobby` - User's hobbies.

**Dataset Preparation:**
- Data is processed by creating numeric mappings for `Profession` and `Activity Description`.
- Data is split into train and test using `train_test_split`.

## Libraries used ##
This project uses the following libraries for various purposes:

### 1. Data Manipulation and Analysis ###
- pandas
### Deep Learning ###
- tensorflow (including components: tensorflow.keras.layers, tensorflow.keras.models, tensorflow.keras.callbacks)
### Machine Learning and Evaluation ###
- scikit-learn (includes components: train_test_split, mean_squared_error)
### Interactivity and Visualization ###
- ipywidgets (includes components: widgets, interact)

### Code implementation ###
The following libraries are imported in the code:
- import pandas as pd
- import tensorflow as tf
- import ipywidgets as widgets
- from tensorflow.keras import layers, models
- from sklearn.model_selection import train_test_split
- from sklearn.metrics import mean_squared_error
- from tensorflow.keras.callbacks import EarlyStopping
- from IPython.display import display
- from ipywidgets import interact

### Training the Model ### 
- The training data is processed using `EarlyStopping` to avoid overfitting.
- The model is trained to predict the relationship between profession and activity.

### Model Storage ### 
- The trained model is saved as a `.tflite` file:
     ```python
     model.save('to_do_list.tflite')
     ```
- This file is submitted to the cloud computing team for API integration.
