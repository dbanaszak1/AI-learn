import pandas as pd
from sklearn.preprocessing import LabelEncoder
from joblib import load

# Model and encoders load
model = load('decision_tree_model.joblib')
label_encoders = load('label_encoders.joblib')

# Test data
new_data = {
    'weather': 'clear',
    'season': 'winter',
    'last_pickup': 1,
    'space_in_truck': 1,
    'trash_type': 'BIO',
    'temp': 10,
    'can_pickup_avilable': 1,
    'can_actual_capacity': 10
}

# Data convert
encoded_data = {}
for column, value in new_data.items():
    if column in label_encoders:
        encoded_value = label_encoders[column].transform([value])[0]
    else:
        encoded_value = value
    encoded_data[column] = encoded_value

# encoded_data to DataFrame convert
encoded_data_df = pd.DataFrame([encoded_data])

# Prediction
prediction = model.predict(encoded_data_df)
print(prediction[0])
print(f'Decyzja: {"Take" if prediction[0] == 1 else "Not Take"}')
