import pandas as pd
import tensorflow as tf
from tensorflow import keras
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
data = pd.read_csv('Churn_Modelling.csv')
X = data.drop(columns=['Exited', 'CustomerId', 'Surname', 'RowNumber'])
Exclude columns
y = data['Exited'] # Target
#
# Step 3: Data Preprocessing
# Handle missing values and encode categorical variables
# Removing rows with missing values:
data = data.drop(['CustomerId', 'Surname', 'RowNumber'], axis = 1)
print(data.columns)
# Replacing missing values with a specific value (e.g., mean):
# data['column_name'].fillna(data['column_name'].mean(), inplace=True)
Index(['CreditScore', 'Geography', 'Gender', 'Age', 'Tenure', 'Balance',
'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary',
'Exited'],
dtype='object')
# You need to ensure that the columns 'Geography' and 'Gender' are present in
the DataFrame X
# Add additional error handling to verify the column names
columns_to_encode = ['Geography', 'Gender']
for column in columns_to_encode:
if column not in X.columns:
raise ValueError(f"Column '{column}' not found in the DataFrame X.")
# You need to encode categorical variables like "Geography" and "Gender" into
numerical format using one-hot encoding.
X = pd.get_dummies(X, columns=['Geography', 'Gender'], drop_first=True)
scaler = MinMaxScaler()
X = scaler.fit_transform(X)
# Step 5: Initialize and Build the Model
model = keras.Sequential([
keras.layers.Dense(64, activation='relu', input_shape=(X.shape[1],)),
keras.layers.Dense(32, activation='relu'),
keras.layers.Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy',
metrics=['accuracy'])
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
random_state=42)
# Train the model
model.fit(X_train, y_train, epochs=20, batch_size=32, verbose=1)
# Epoch 1/20
# 250/250 [==============================] - 1s 2ms/step - loss: 0.4769 -
# accuracy: 0.7947
# Epoch 2/20
# 250/250 [==============================] - 1s 2ms/step - loss: 0.4413 -
# accuracy: 0.8098
# Epoch 3/20
# 250/250 [==============================] - 1s 2ms/step - loss: 0.4229 -
# accuracy: 0.8200
# Epoch 4/20
# 250/250 [==============================] - 0s 2ms/step - loss: 0.4007 -
# accuracy: 0.8299
# Epoch 5/20
# 250/250 [==============================] - 1s 3ms/step - loss: 0.3800 -
# accuracy: 0.8406
# Epoch 6/20
# 250/250 [==============================] - 1s 3ms/step - loss: 0.3663 -
# accuracy: 0.8486
# Epoch 7/20
# 250/250 [==============================] - 0s 2ms/step - loss: 0.3593 -
# accuracy: 0.8511
# Epoch 8/20
# 250/250 [==============================] - 0s 2ms/step - loss: 0.3537 -
# accuracy: 0.8551
# Epoch 9/20
# 250/250 [==============================] - 0s 2ms/step - loss: 0.3502 -
# accuracy: 0.8575
# Epoch 10/20
# 250/250 [==============================] - 0s 2ms/step - loss: 0.3482 -
# accuracy: 0.8574
# Epoch 11/20
# 250/250 [==============================] - 0s 2ms/step - loss: 0.3450 -
# accuracy: 0.8585
# Epoch 12/20
# 250/250 [==============================] - 1s 3ms/step - loss: 0.3435 -
# accuracy: 0.8581
# Epoch 13/20
# 250/250 [==============================] - 1s 2ms/step - loss: 0.3411 -
# accuracy: 0.8612
# Epoch 14/20
# 250/250 [==============================] - 1s 2ms/step - loss: 0.3412 -
# accuracy: 0.8601
# Epoch 15/20
# 250/250 [==============================] - 1s 5ms/step - loss: 0.3378 -
# accuracy: 0.8610
# Epoch 16/20
# 250/250 [==============================] - 1s 6ms/step - loss: 0.3371 -
# accuracy: 0.8605
# Epoch 17/20
# 250/250 [==============================] - 1s 5ms/step - loss: 0.3364 -
# accuracy: 0.8608
# Epoch 18/20
# 250/250 [==============================] - 1s 6ms/step - loss: 0.3366 -
# accuracy: 0.8612
# Epoch 19/20
# 250/250 [==============================] - 1s 5ms/step - loss: 0.3348 -
# accuracy: 0.8604
# Epoch 20/20
# 250/250 [==============================] - 1s 5ms/step - loss: 0.3326 -
# accuracy: 0.8634
# <keras.callbacks.History at 0x1ebc037af40>
# Step 6: Evaluate the Model
y_pred = model.predict(X_test)
y_pred = (y_pred > 0.5).astype(int)
# Convert to binary prediction
# 63/63 [==============================] - 0s 2ms/step
accuracy = accuracy_score(y_test, y_pred)
confusion = confusion_matrix(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print("Confusion Matrix:")
print(confusion)
# Accuracy: 0.86
# Confusion Matrix:
# [[1557
# 50]
# [ 230 163]]
