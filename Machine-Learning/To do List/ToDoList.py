import pandas as pd
import tensorflow as tf
import ipywidgets as widgets
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from tensorflow.keras.callbacks import EarlyStopping
from IPython.display import display
from ipywidgets import interact

df = pd.read_csv('updated_activities_dataset.csv')

Profesi = {user: idx for idx, user in enumerate(df['Profession'].unique())}
df['user_Profession'] = df['Profession'].map(Profesi)

Activity = {item: idx for idx, item in enumerate(df['Activity Description'].unique())}
df['user_Activity'] = df['Activity Description'].map(Activity)

interactions = df[['user_Profession', 'user_Activity']].values

num_profession = len(Profesi)
num_Activity = len(Activity)

Profession_input = layers.Input(shape=(1,), name='Profession')
Activity_input = layers.Input(shape=(1,), name='Activity')

Profession_embedding = layers.Embedding(
    input_dim=num_profession,
    output_dim=10,
    embeddings_initializer='uniform',
)(Profession_input)

Activity_embedding = layers.Embedding(
    input_dim=num_Activity,
    output_dim=10,
    embeddings_initializer='uniform',
)(Activity_input)

dot_product = layers.Dot(axes=2)([Profession_embedding, Activity_embedding])

flattened = layers.Flatten()(dot_product)

output = layers.Dense(1, activation='sigmoid')(flattened)

model = models.Model(inputs=[Profession_input, Activity_input], outputs=output)

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

X_train, X_test = train_test_split(interactions, test_size=0.2, random_state=42)

train_user = X_train[:, 0]
test_user = X_test[:, 0]
train_item = X_train[:, 1]
test_item = X_test[:, 1]

early_stopping = EarlyStopping(monitor='accuracy',
                               patience=1,
                               mode='max',
                               baseline=0.90,
                               restore_best_weights=True)

model.fit([train_user, train_item], tf.ones(len(train_user)), epochs=10, batch_size=32, callbacks=[early_stopping])

predictions = model.predict([test_user, test_item])

mse = mean_squared_error(tf.ones(len(predictions)), predictions)
print(f'Mean Squared Error: {mse}')


# Fungsi untuk menampilkan rekomendasi berdasarkan profesi dan hobi
def show_recommendation(Profession, Hobby):
    # Filter data berdasarkan profesi dan hobi
    filtered_df = df[(df['Profession'] == Profession) & (df['Hobby'] == Hobby)]

    # Tampilkan rekomendasi kegiatan yang cocok
    recommendations = filtered_df[['Activity Description']].head(5)  # Ambil 5 rekomendasi pertama
    print("Recommended Activities:")
    for index, row in recommendations.iterrows():
        print(f"- {row['Activity Description']}")

# Membuat dropdown untuk profesi dan hobi
Profession_dropdown = widgets.Dropdown(
    options=df['Profession'].unique(),
    description='Profession:',
    disabled=False
)

Hobby_dropdown = widgets.Dropdown(
    options=df['Hobby'].unique(),
    description='Hobby:',
    disabled=False
)

# Menghubungkan dropdown dengan fungsi show_recommendation
interact(show_recommendation, Profession=Profession_dropdown, Hobby=Hobby_dropdown)
