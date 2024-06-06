import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

file_path = 'treedata.csv'
data = pd.read_csv(file_path)

# Data translating to numeric values
label_encoders = {}
for column in data.columns:
    if data[column].dtype == object:
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column])
        label_encoders[column] = le

X = data.drop('take_away_decison', axis=1)
y = data['take_away_decison']

# Tree test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = DecisionTreeClassifier(criterion='entropy', random_state=42)
model.fit(X_train, y_train)

plt.figure(figsize=(20,10))
plot_tree(model, feature_names=X.columns, class_names=['Not Take', 'Take'], filled=True)
plt.show()
