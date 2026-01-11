from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("kidney_model.pkl", "rb"))

# ---- Helper functions ----
def calculate_egfr(scr, age, gender="male"):
    """Calculate estimated Glomerular Filtration Rate (eGFR)"""
    if gender == "male":
        return 175 * (scr ** -1.154) * (age ** -0.203)
    else:
        return 175 * (scr ** -1.154) * (age ** -0.203) * 0.742

def get_ckd_stage(egfr):
    """Return CKD stage based on eGFR value"""
    if egfr >= 90:
        return "Stage 1"
    elif egfr >= 60:
        return "Stage 2"
    elif egfr >= 30:
        return "Stage 3"
    elif egfr >= 15:
        return "Stage 4"
    else:
        return "Stage 5"

# ---- Home page ----
@app.route('/')
def home():
    return render_template('index.html')

# ---- Prediction route ----
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form values
        sg = float(request.form['sg'])
        al = float(request.form['al'])
        sc = float(request.form['sc'])
        hemo = float(request.form['hemo'])
        age = float(request.form.get('age', 50))  # Optional: default 50 if not provided
        gender = request.form.get('gender', 'male')  # Optional gender for eGFR

        # Prepare features for model
        features = np.array([[sg, al, sc, hemo]])

        # Make prediction
        prediction_class = model.predict(features)[0]

        # Calculate eGFR and CKD stage only if CKD detected
        if prediction_class == 1:
            egfr = calculate_egfr(sc, age, gender)
            stage = get_ckd_stage(egfr)
            prediction_text = "Chronic Kidney Disease Detected"
        else:
            egfr = None
            stage = None
            prediction_text = "No Chronic Kidney Disease Detected"

        return render_template(
            'result.html',
            prediction=prediction_text,
            sc=sc,
            egfr=round(egfr, 2) if egfr else None,
            stage=stage
        )

    except Exception as e:
        return render_template('result.html', prediction=f"Error: {str(e)}")

# ---- Run app ----
if __name__ == "__main__":
    app.run(debug=True)