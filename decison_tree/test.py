import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Test data
data = pd.DataFrame({
    'weather': ['clear', 'rain', 'snow', 'clear', 'rain'],
    'season': ['summer', 'summer', 'winter', 'spring', 'autumn'],
    'last_pickup': [2, 7, 3, 10, 5],
    'space_in_truck': [1, 0, 1, 1, 1],
    'trash_type': ['plastic', 'BIO', 'mixed', 'paper', 'glass'],
    'temp': [25, 30, -5, 15, 10],
    'can_pickup_avilable': [1, 1, 0, 1, 1],
    'can_actual_capacity': [50, 10, 70, 80, 90],
    'take_away_decison': [1, 1, 0, 1, 1]
})

print("Przed kodowaniem:")
print(data)

# Data translating to numeric values
label_encoders = {}
for column in data.columns:
    if data[column].dtype == object:
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column])
        label_encoders[column] = le

print("\nPo kodowaniu:")
print(data)

# Example map
print("\nMapowanie dla 'weather':")
for i, item in enumerate(label_encoders['weather'].classes_):
    print(f"{item} -> {i}")
