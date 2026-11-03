import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import os
import joblib

class PlacementRiskPredictor:
    def __init__(self):
        self.model = None
        self.model_path = os.path.join(os.path.dirname(__file__), 'risk_model.pkl')
        self.load_model()

    def load_model(self):
        if os.path.exists(self.model_path):
            try:
                self.model = joblib.load(self.model_path)
            except Exception as e:
                print(f"Error loading model: {e}")
                self.model = None

    def train_dummy_model(self):
        # Create some dummy data for initial training if no model exists
        # Features: [CGPA, Arrears, Hackathons, Internship]
        X = np.array([
            [9.0, 0, 5, 2], [8.5, 0, 3, 1], [8.0, 1, 2, 1], [7.5, 2, 1, 0],
            [6.0, 5, 0, 0], [5.5, 6, 0, 0], [7.0, 2, 1, 0], [9.5, 0, 6, 3]
        ])
        # Labels: 0=Low Risk, 1=Medium Risk, 2=High Risk
        y = np.array([0, 0, 1, 1, 2, 2, 1, 0])
        
        self.model = RandomForestClassifier(n_estimators=10)
        self.model.fit(X, y)
        
        # Save the model
        joblib.dump(self.model, self.model_path)
        print("Dummy model trained and saved.")

    def predict_risk(self, cgpa, arrears, mock_test_score, internship_count):
        # If model is not loaded, train a dummy one
        if self.model is None:
            self.train_dummy_model()
        
        # Normalize/Preprocess input
        # Assuming mock_test_score is out of 100, we might want to scale it or usage as is
        # The dummy model used 'Hackathons' as 3rd feature, let's map mock_test_score/20 to it for now
        # Features: [CGPA, Arrears, Hackathons-proxy, Internship]
        features = np.array([[cgpa, arrears, int(mock_test_score/20), internship_count]])
        
        try:
            prediction = self.model.predict(features)[0]
            probability = self.model.predict_proba(features)[0]
            
            risk_labels = {0: 'Low Risk', 1: 'Medium Risk', 2: 'High Risk'}
            return risk_labels.get(prediction, 'Unknown'), probability
        except Exception as e:
            print(f"Prediction error: {e}")
            return "Unknown", []

predictor = PlacementRiskPredictor()
