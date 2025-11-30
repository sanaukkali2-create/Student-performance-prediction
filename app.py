
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

model = joblib.load("student_model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    arr = np.array([[data['hours'], data['attendance'], data['previous_score']]])
    prediction = model.predict(arr)[0]
    return jsonify({"pass": int(prediction)})

if __name__ == "__main__"
    app.run(port=5002)
