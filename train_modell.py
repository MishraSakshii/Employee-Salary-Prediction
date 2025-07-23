import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import joblib

# 1. Load dataset
df = pd.read_csv('employee_data.csv')  # Replace with your actual file name

# 2. Select features and target
features = [
    "Age", "Distance From Home", "Education",
    "Job Level", "Monthly Income", "Percent Salary Hike",
    "Stock Option Level", "Total Working Years", "Years At Company"
]

X = df[features]
y = df["Salary Class"]  # Make sure this column exists in your dataset

# 3. Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5. Train KNN model
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train_scaled, y_train)

# 6. Evaluate
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# 7. Save model and scaler
joblib.dump(model, 'knn_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
print("Model and scaler saved successfully.")
