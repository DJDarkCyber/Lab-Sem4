import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
# Input variables
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# Target variable
y = np.array([[0], [1], [1], [0]])
# Example input values
# Example output values
# Model 1: Shallow Neural Network
model_1 = Sequential()
model_1.add(Dense(10, input_dim=2, activation='relu'))
model_1.add(Dense(1, activation='sigmoid'))
model_1.compile(loss='binary_crossentropy', optimizer='adam',
metrics=['accuracy'])
# Model 2: Deep Neural Network
model_2 = Sequential()
model_2.add(Dense(20, input_dim=2, activation='relu'))
model_2.add(Dense(10, activation='relu'))
model_2.add(Dense(1, activation='sigmoid'))
model_2.compile(loss='binary_crossentropy', optimizer='adam',
metrics=['accuracy'])
# Model 3: Deep Neural Network with Dropout
model_3 = Sequential()
model_3.add(Dense(20, input_dim=2, activation='relu'))model_3.add(Dropout(0.2))
model_3.add(Dense(10, activation='relu'))
model_3.add(Dropout(0.2))
model_3.add(Dense(1, activation='sigmoid'))
model_3.compile(loss='binary_crossentropy', optimizer='adam',
metrics=['accuracy'])
# Train and evaluate Model 1
model_1.fit(X, y, epochs=5, batch_size=4)
loss_1, accuracy_1 = model_1.evaluate(X, y)
print("Model 1 - Loss:", loss_1)
print("Model 1 - Accuracy:", accuracy_1)
print("--------------------")
# Train and evaluate Model 2
model_2.fit(X, y, epochs=5, batch_size=4)
loss_2, accuracy_2 = model_2.evaluate(X, y)
print("Model 2 - Loss:", loss_2)
print("Model 2 - Accuracy:", accuracy_2)
print("--------------------")
# Train and evaluate Model 3
model_3.fit(X, y, epochs=5, batch_size=4)
loss_3, accuracy_3 = model_3.evaluate(X, y)
print("Model 3 - Loss:", loss_3)
print("Model 3 - Accuracy:", accuracy_3)
print("--------------------")
