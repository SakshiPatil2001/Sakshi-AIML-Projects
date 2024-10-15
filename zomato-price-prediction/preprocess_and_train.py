import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib
import os

# Step 1: Load the dataset
try:
    df = pd.read_csv(r'C:\Users\saksh\OneDrive\Desktop\zomato-price-prediction\dataset\zomato.csv')
except FileNotFoundError:
    print("The specified file was not found. Please check the file path and try again.")
    exit()

# Step 2: Rename columns to match required features
df.rename(columns={'rate (out of 5)': 'rating', 'num of ratings': 'votes', 'avg cost (two people)': 'avg_cost_for_two'}, inplace=True)

# Step 3: Keep only necessary columns
df['is_veg'] = df['cuisines type'].apply(lambda x: 1 if 'Vegetarian' in x else 0)
required_columns = ['rating', 'votes', 'is_veg', 'avg_cost_for_two']
df = df[required_columns]

# Step 4: Handle missing values
df = df.dropna()

# Step 5: Define features and target variable
features = df[['rating', 'votes', 'is_veg']]
target = df['avg_cost_for_two']

# Step 6: Train-test split
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Step 7: Model training
model = LinearRegression()
model.fit(X_train, y_train)

# Step 8: Make predictions
y_pred = model.predict(X_test)

# Step 9: Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Step 10: Save the model
os.makedirs('models', exist_ok=True)
joblib.dump(model, 'models/zomato_price_predictor.pkl')
print("Model saved successfully.")






