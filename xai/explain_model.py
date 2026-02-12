import pandas as pd
import joblib
from xai_engine import XAIEngine

# -----------------------------------------
# Load Trained Model
# -----------------------------------------
model = joblib.load("models/fraud_model.pkl")


# IMPORTANT:
# These must match the features used in train_model.py
feature_names = ["amount", "time", "location_risk", "merchant_risk", "pin_attempts"]

# Initialize XAI Engine
engine = XAIEngine(model, feature_names)


# =========================================
# FUNCTION TO TEST ANY TRANSACTION
# =========================================
def test_transaction(transaction_dict):
    transaction_df = pd.DataFrame([transaction_dict])
    explanation = engine.generate_local_explanation(transaction_df)

    print("\n==============================")
    print("      XAI EXPLANATION")
    print("==============================\n")

    for key, value in explanation.items():
        print(f"{key}: {value}")


# =========================================
# TEST CASE 1 → SAFE TRANSACTION
# =========================================
safe_transaction = {
    "amount": 500,
    "time": 3,
    "location_risk": 1,
    "merchant_risk": 1,
    "pin_attempts": 1
}

test_transaction(safe_transaction)


# =========================================
# TEST CASE 2 → HIGH RISK / FRAUD
# =========================================
fraud_transaction = {
    "amount": 150000,        # > 1 Lakh
    "time": 2,
    "location_risk": 4,
    "merchant_risk": 4,
    "pin_attempts": 5        # > 3 attempts
}

test_transaction(fraud_transaction)
