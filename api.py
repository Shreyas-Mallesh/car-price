import json
import pickle
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)


# Define API endpoint for predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Parse input data from JSON request
    data = request.get_json()
    X = np.array(data['features']).reshape(1, -1)

    # Make prediction using trained model
    y_pred = model.predict(X)

    # Format prediction result as JSON response
    response = {
        'prediction': float(y_pred[0])
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
