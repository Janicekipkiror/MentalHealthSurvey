from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load model and encoder
model = pickle.load(open("model.pkl", "rb"))
encoder = pickle.load(open("target_encoder.pkl", "rb"))

FEATURE_ORDER = [
    'gender',
    'age',
    'cgpa',
    'academic_pressure',
    'financial_concerns',
    'social_relationships',
    'study_satisfaction'
]

@app.route('/')
def home():
    return "Mental Health Prediction API Running"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json

        
        input_df = pd.DataFrame([data])

        
        input_df = input_df[FEATURE_ORDER]

        
        prediction = model.predict(input_df)

        
        result = encoder.inverse_transform(prediction)

        return jsonify({'risk_level': str(result[0])})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)