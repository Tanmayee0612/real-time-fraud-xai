import numpy as np


class XAIEngine:
    def __init__(self, model, feature_names):
        """
        model: trained ML model (RandomForest, etc.)
        feature_names: list of feature column names
        """
        self.model = model
        self.feature_names = feature_names

    # --------------------------------------------------
    # Prediction Layer (DOES NOT MODIFY MODEL LOGIC)
    # --------------------------------------------------
    def predict_transaction(self, transaction_df):
        """
        Returns prediction and fraud probability
        """
        prediction = self.model.predict(transaction_df)[0]
        probability = self.model.predict_proba(transaction_df)[0][1]

        return prediction, probability

    # --------------------------------------------------
    # Risk Level Categorization
    # --------------------------------------------------
    def risk_level(self, probability):
        if probability > 0.8:
            return "High Risk"
        elif probability > 0.4:
            return "Medium Risk"
        else:
            return "Low Risk"

    # --------------------------------------------------
    # Main Local Explanation Function
    # --------------------------------------------------
    def generate_local_explanation(self, transaction_df):
        prediction, probability = self.predict_transaction(transaction_df)

        explanation = {
            "Prediction": "Fraud" if prediction == 1 else "Not Fraud",
            "Fraud Probability": round(float(probability), 3),
            "Risk Level": self.risk_level(probability),
            "Red Flags": [],
            "Feature Analysis": {},
            "Recommendation": ""
        }

        row = transaction_df.iloc[0]

        # --------------------------------------------------
        # Advanced Red Flag Interpretation Layer
        # (This is YOUR XAI intelligence layer)
        # --------------------------------------------------

        # 1️⃣ Very High Amount Check
        if "amount" in row and row["amount"] > 100000:
            explanation["Red Flags"].append(
                "Extremely high transaction amount (> 1 Lakh)"
            )

        # 2️⃣ Multiple Wrong PIN Attempts
        if "pin_attempts" in row and row["pin_attempts"] > 3:
            explanation["Red Flags"].append(
                "Multiple failed PIN attempts detected"
            )

        # 3️⃣ Suspicious Location
        if "location_risk" in row and row["location_risk"] > 2:
            explanation["Red Flags"].append(
                "Transaction from high-risk location"
            )

        # 4️⃣ Suspicious Merchant
        if "merchant_risk" in row and row["merchant_risk"] > 2:
            explanation["Red Flags"].append(
                "Transaction with high-risk merchant"
            )

        # --------------------------------------------------
        # Feature-Level Interpretation
        # --------------------------------------------------

        for feature in self.feature_names:
            if feature not in row:
                continue

            value = row[feature]

            if feature == "amount":
                if value > 100000:
                    explanation["Feature Analysis"][feature] = (
                        "Unusually high transaction value"
                    )
                elif value > 200:
                    explanation["Feature Analysis"][feature] = (
                        "Moderately high transaction amount"
                    )
                else:
                    explanation["Feature Analysis"][feature] = (
                        "Normal transaction amount"
                    )

            elif feature == "pin_attempts":
                if value > 3:
                    explanation["Feature Analysis"][feature] = (
                        "Multiple incorrect PIN entries"
                    )
                else:
                    explanation["Feature Analysis"][feature] = (
                        "Normal PIN verification"
                    )

            elif feature == "location_risk":
                if value > 2:
                    explanation["Feature Analysis"][feature] = (
                        "High risk geographical region"
                    )
                else:
                    explanation["Feature Analysis"][feature] = (
                        "Safe transaction region"
                    )

            elif feature == "merchant_risk":
                if value > 2:
                    explanation["Feature Analysis"][feature] = (
                        "Suspicious merchant category"
                    )
                else:
                    explanation["Feature Analysis"][feature] = (
                        "Trusted merchant category"
                    )

            else:
                explanation["Feature Analysis"][feature] = f"Observed value: {value}"

        # --------------------------------------------------
        # Recommendation Layer (Advanced Banking Style)
        # --------------------------------------------------

        if prediction == 1 or len(explanation["Red Flags"]) > 0:
            explanation["Recommendation"] = (
                "⚠️ Transaction should be reviewed manually."
            )
        else:
            explanation["Recommendation"] = (
                "✅ Transaction appears safe."
            )

        return explanation
