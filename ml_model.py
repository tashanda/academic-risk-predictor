import numpy as np
from sklearn.linear_model import LinearRegression


# Features:
# [study_hours, current_grade, difficulty, missing_assignments, attendance, sleep_hours]
# difficulty: 1 = easy, 4 = extreme
# attendance: 0–100 (%)
# sleep_hours: hours per night (0–10)

X = np.array([
    [1, 52, 4, 6, 60, 5],
    [2, 55, 4, 5, 65, 5],
    [3, 58, 4, 5, 68, 6],
    [4, 62, 4, 4, 70, 6],
    [5, 65, 4, 4, 73, 6],
    [6, 68, 4, 3, 75, 7],

    [1, 55, 3, 5, 68, 5],
    [2, 58, 3, 4, 70, 6],
    [3, 62, 3, 4, 74, 6],
    [4, 66, 3, 3, 78, 7],
    [5, 70, 3, 3, 82, 7],
    [6, 74, 3, 2, 86, 7],
    [7, 78, 3, 2, 88, 8],

    [2, 60, 2, 4, 75, 6],
    [3, 64, 2, 3, 78, 6],
    [4, 68, 2, 3, 82, 7],
    [5, 72, 2, 2, 85, 7],
    [6, 76, 2, 2, 88, 7],
    [7, 80, 2, 1, 91, 8],
    [8, 84, 2, 1, 94, 8],
    [9, 88, 2, 0, 96, 8],

    [2, 65, 1, 3, 82, 6],
    [3, 70, 1, 2, 85, 7],
    [4, 74, 1, 2, 88, 7],
    [5, 78, 1, 1, 91, 7],
    [6, 82, 1, 1, 94, 8],
    [7, 86, 1, 0, 96, 8],
    [8, 90, 1, 0, 97, 8],
    [9, 94, 1, 0, 98, 8],
    [10, 96, 1, 0, 99, 8]
])

# Simulated output
# future_grade =
# current_grade
# + (study_hours * 2)
# - (difficulty * 5)
# - (missing_assignments * 3)
# + ((attendance - 75) * 0.2)
# + ((sleep_hours - 6) * 1.5)

Y = np.array([
    12, 23, 30, 40, 45, 55,
    22, 35, 42, 53, 60, 70, 77,
    40, 52, 60, 70, 78, 88, 95, 100,
    47, 63, 71, 82, 90, 100, 100, 100, 100
])

# Train the model
model = LinearRegression()
model.fit(X, Y)

# Function to predict academic risk
def predict_risk(study_hours, current_grade, difficulty, missing_assignments, attendance, sleep_hours):
    input_data = [[study_hours, current_grade, difficulty, missing_assignments, attendance, sleep_hours]]
    predicted_grade = model.predict(input_data)[0]

    predicted_grade = max(0, min(predicted_grade, 100))

    if predicted_grade < 60:
        risk = "High Risk"
        recommendation = "Increase study hours, improve sleep, reduce missing assignments, and seek help."
    elif predicted_grade < 75:
        risk = "Moderate Risk"
        recommendation = "Improve consistency, maintain good sleep habits, and reduce missed work."
    else:
        risk = "Low Risk"
        recommendation = "Maintain your current habits and stay consistent."

    return {
        "predicted_grade": round(float(predicted_grade), 2),
        "risk": risk,
        "recommendation": recommendation
    }

# Test function with sample inputs (commented out for production)
# print(predict_risk(5, 70, 2))
# print(predict_risk(2, 55, 3))
# print(predict_risk(5, 93, 1))







