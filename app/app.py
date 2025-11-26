from flask import Flask, request, render_template
import joblib
import numpy as np
import pandas as pd
import os

app = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))
model_path = os.path.join(basedir, '../models/random_forest_model.joblib')
scaler_path = os.path.join(basedir, '../models/scaler.joblib')

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
       
      
        form_data = {
            'College': int(request.form['College']),
            'City': int(request.form['City']),
            'Previous CTC': float(request.form['Previous CTC']),
            'Previous job change': int(request.form['Previous job change']),
            'Graduation Marks': int(request.form['Graduation Marks']),
            'EXP (Month)': int(request.form['EXP (Month)']),
            'Role_Manager': int(request.form['Role'])
        }
        
        # --- Create DataFrame for prediction ---
        # The order of columns MUST match the order during training
        features = pd.DataFrame([form_data], columns=[
            'College', 'City', 'Previous CTC', 'Previous job change', 
            'Graduation Marks', 'EXP (Month)', 'Role_Manager'
        ])

       
        scaled_features = scaler.transform(features)

       
        prediction = model.predict(scaled_features)
        
       
        output = f'{prediction[0]:,.2f}'

        return render_template('index.html', prediction_text=f'Predicted Salary (CTC): ₹ {output}')

    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {e}')

if __name__ == "__main__":
    app.run(debug=True)
