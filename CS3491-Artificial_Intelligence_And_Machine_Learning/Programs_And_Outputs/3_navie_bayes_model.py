import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

df = pd.read_csv("https://raw.githubusercontent.com/DJDarkCyber/Lab-Sem4/main/CS3491_Artificial_Intelligence_And_Machine_Learning/Programs_And_Outputs/data/data.csv")

X = df.drop('buy_computer', axis=1)
y = df['buy_computer']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = GaussianNB()
model.fit(X_train.values, y_train.values)
print(f"Accuracy : {model.score(X_test.values, y_test.values)}")

new_data = np.array([[35, 60000, 1, 100]])
prediction = model.predict(new_data)
print("Prediction: ", prediction)
