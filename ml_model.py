import numpy as np


def predict_risk(features):
    # Example placeholder logic for academic risk prediction
    # Replace with a trained model or more complex logic.
    attendance = float(features.get('attendance', 0))
    assignments = float(features.get('assignments', 0))
    sleep = float(features.get('sleep_hours', 0))

    score = 0.4 * (100 - attendance) + 0.4 * (100 - assignments) + 0.2 * max(0, 8 - sleep) * 12.5
    return round(min(max(score, 0), 100), 2)
