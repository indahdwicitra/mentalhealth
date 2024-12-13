import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Dense, Dropout, Conv1D, GlobalMaxPooling1D
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
import re
import string
from sklearn.model_selection import train_test_split

# Load the dataset
df = pd.read_csv('capstone/data/emotion_sentimen_dataset.csv')

# Fill missing values in the 'Emotion' column with the mode
modus = df['Emotion'].mode()[0]
df['Emotion'] = df['Emotion'].fillna(modus)

# Display dataset info
df.info()

# Display value counts for 'Emotion'
df['Emotion'].value_counts()

# Function to determine sentiment based on text polarity
def getSubjectivity(text):
    obj = TextBlob(text)
    polarity = obj.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Apply the sentiment function to the text column
df['Sentimen'] = df['text'].apply(getSubjectivity)

# Function to clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Clean the text column
df['text'] = df['text'].apply(clean_text)

# Features and labels
X_feature = df['text']
y_label = df['Sentimen']

# Tokenize text
tokenizer = Tokenizer(num_words=5000, oov_token='<OOV>')
tokenizer.fit_on_texts(X_feature)
X_seq = tokenizer.texts_to_sequences(X_feature)

# Pad sequences
max_length = 100
X_padded = pad_sequences(X_seq, maxlen=max_length, padding='post', truncating='post')

# Convert labels to one-hot encoding
y_onehot = pd.get_dummies(y_label).values

# Train-test split
x_train, x_test, y_train, y_test = train_test_split(X_padded, y_onehot, test_size=0.3, random_state=42)

# Build the model
model = Sequential([
    tf.keras.layers.Input(shape=(max_length,), dtype=tf.int32),
    Embedding(input_dim=5000, output_dim=32, input_length=max_length),
    Conv1D(64, kernel_size=3, activation='relu'),
    GlobalMaxPooling1D(),
    Dense(16, activation='relu'),
    Dropout(0.3),
    Dense(3, activation='softmax')
])

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

# Custom callback to stop training at target accuracy
class StopAtAccuracy(tf.keras.callbacks.Callback):
    def __init__(self, target_accuracy=0.95):
        super().__init__()
        self.target_accuracy = target_accuracy

    def on_epoch_end(self, epoch, logs=None):
        if logs.get("accuracy") >= self.target_accuracy:
            print(f"\nEpoch {epoch+1}: Target accuracy reached. Stopping training.")
            self.model.stop_training = True

# Train the model
early_stopping = StopAtAccuracy(target_accuracy=0.95)
history = model.fit(
    x_train, y_train,
    validation_data=(x_test, y_test),
    epochs=5,
    callbacks=[early_stopping]
)

# Evaluate the model
loss, accuracy = model.evaluate(x_test, y_test)
print(f"Loss: {loss}, Accuracy: {accuracy}")

# Plot training history
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.title('Training and Validation Accuracy')
plt.show()

plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.title('Training and Validation Loss')
plt.show()

# Test predictions
test_texts = ["I love this!", "This is awful.", "It's neutral."]
test_texts_seq = tokenizer.texts_to_sequences(test_texts)
test_texts_padded = pad_sequences(test_texts_seq, maxlen=max_length, padding='post')

predictions = model.predict(test_texts_padded)
predicted_classes = tf.argmax(predictions, axis=1).numpy()

for text, sentiment in zip(test_texts, predicted_classes):
    print(f"Text: {text}")
    print(f"Predicted Sentiment: {['Negative', 'Neutral', 'Positive'][sentiment]}\n")

# Save the model
model.save('model.keras')

# Convert to TFLite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save TFLite model
with open('emotion_model.tflite', 'wb') as f:
    f.write(tflite_model)
