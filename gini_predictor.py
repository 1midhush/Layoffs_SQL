import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeRegressor

# Load the dataset
data = pd.read_csv('clean_layoffs.csv')

# Display the first few rows of the dataframe
print(data.head())

# Drop rows with missing percentage_laid_off values for training
data = data.dropna(subset=['percentage_laid_off'])

# Encode categorical features as strings to avoid mixed data types
categorical_columns = ['industry', 'stage', 'country']
for column in categorical_columns:
    data[column] = data[column].astype(str)

# Apply label encoding to the categorical features
label_encoders = {}
for column in categorical_columns:
    label_encoders[column] = LabelEncoder()
    data[column] = label_encoders[column].fit_transform(data[column])

# Separate features (X) and target (y)
X = data.drop('percentage_laid_off', axis=1)
y = data['percentage_laid_off']

# Initialize and train the decision tree regressor
regressor = DecisionTreeRegressor()
regressor.fit(X, y)

# Example input for prediction
input_data = {
    'industry': 'Healthcare',
    'total_laid_off': 100,
    'stage': 'Post-IPO',
    'country': 'United States',
    'funds_raised_millions': 242
}

# Convert the input data to a dataframe
input_df = pd.DataFrame([input_data])

# Encode the input data
for column in categorical_columns:
    input_df[column] = label_encoders[column].transform(input_df[column].astype(str))

# Predict the percentage_laid_off
predicted_percentage = regressor.predict(input_df)
print(f"Predicted percentage laid off: {predicted_percentage[0]}")
