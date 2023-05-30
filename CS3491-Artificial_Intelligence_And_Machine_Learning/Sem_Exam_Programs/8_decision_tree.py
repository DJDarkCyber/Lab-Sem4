import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree
# Read the data
data = pd.read_csv('flowers.csv')
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values
# Encode the labels
le = LabelEncoder()
y = le.fit_transform(y)
# Create and fit a decision tree model
tree = DecisionTreeClassifier()
tree.fit(X, y)
# Define the desired input for prediction
desired_input = np.array([[5.1, 3.5, 1.4, 0.2]])
based on your desired input
# Modify the values
# Predict the output for the desired input
predicted_output = le.inverse_transform(tree.predict(desired_input))
print("Predicted output:", predicted_output)
# Visualize the decision tree
plt.figure(figsize=(10, 6))
plot_tree(tree, filled=True)
plt.title("Decision Tree")
plt.show()
