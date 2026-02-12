import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import os

# -----------------------------------------
# Create Synthetic Fraud Dataset
# -----------------------------------------

np.random.seed(42)
n_samples = 5000

data = pd.DataFrame({
    "amount": np.random.uniform(10, 200000, n_samples),
    "time": np.random.randint(0, 24, n_samples),
    "location_risk": np.random.randint(0, 5, n_samples),
    "merchant_risk": np.random.randint(0, 5, n_samples),
    "pin_attempts": np.random.randint(1, 6, n_samples)  # NEW FEATURE
})

# -----------------------------------------
# Updated Fraud Rule (Advanced)
# -----------------------------------------
# Fraud if:
# amount > 1 lakh AND location_risk > 2 AND pin_attempts > 3

data["fraud"] = (
    (data["amount"] > 100000) &
    (data["location_risk"] > 2) &
    (data["pin_attempts"] > 3)
).astype(int)

# -----------------------------------------
# Split Features & Target
# -----------------------------------------

X = data.drop("fraud", axis=1)
y = data["fraud"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------------------
# Train Model
# -----------------------------------------

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# -----------------------------------------
# Evaluate Model
# -----------------------------------------

y_pred = model.predict(X_test)

print("Model Performance:")
print(classification_report(y_test, y_pred))

# -----------------------------------------
# Save Model
# -----------------------------------------

os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/fraud_model.pkl")

print("Model saved successfully!")
