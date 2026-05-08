# Flask creates the web browser, render_template loads HTML files from your templates folder
# request lets flask read incoming data from the client 
#jsonify converts python data into JSON format to send back to the client for API responses
#predict_risk imports custom ML prediction function from ml_model.py 
from flask import Flask, render_template, request, jsonify
from ml_model import predict_risk

#This initializes the Flask application
app = Flask(__name__)

#When someone visits the website the flask calls the home() func and returns the index.html file to the browser. 
# This is the main page of the website where users can input their data for prediction.
@app.route('/')
def home():
    return render_template('index.html')

# this creates an API endpoint that only accepts POST requests.
@app.route('/predict', methods=['POST'])
def predict():
    #this reads the JSON and converts it into a python dictionary.
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No input provided'}), 400

    #this converts inputs into the correct types
    study_hours = float(data['study_hours'])
    current_grade = float(data['current_grade'])
    difficulty = int(data['difficulty'])
    attendance = float(data['attendance'])
    sleep_hours = float(data['sleep_hours'])
    missing_assignments = int(data['missing_assignments'])

    result = predict_risk(study_hours, current_grade, difficulty, attendance, sleep_hours, missing_assignments)

    return jsonify(result)





if __name__ == '__main__':
    app.run(debug=True)