from flask import Flask, render_template, request, jsonify
from ml_model import predict_risk

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json or {}
    risk = predict_risk(data)
    return jsonify({'risk_score': risk})

if __name__ == '__main__':
    app.run(debug=True)
