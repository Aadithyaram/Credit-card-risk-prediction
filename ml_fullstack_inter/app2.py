from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np
import tensorflow as tf
import joblib

# Load the Random Forest Classifier model
filename = "model2.pkl"
model = joblib.load(filename)

app = Flask(__name__)

# Step 1: Get input on the home page
@app.route('/')
def home():
    return render_template('index.html')

# Step 2: Get additional input on the next page
@app.route('/next', methods=['GET', 'POST'])
def next_page():
    if request.method == 'POST':
        ovd_t1 = int(request.form['ovd_t1'])
        ovd_t2 = request.form.get('ovd_t2')
        ovd_t3 = request.form.get('ovd_t3')
        tovd_sum = int(request.form['ovd_sum'])
        Pay_normal = int(request.form['Pay_normal'])
        prod_code = request.form.get('prod_code')
        prod_limit = int(request.form['prod_limit'])
        new_balance = int(request.form['new_balance'])
        highest_balance = request.form.get('highest_balance')
        
        # Store the collected data in the session
        session['data'] = {
            'ovd_t1': ovd_t1,
            'ovd_t2': ovd_t2,
            'ovd_t3': ovd_t3,
            'tovd_sum': tovd_sum,
            'Pay_normal': Pay_normal,
            'prod_code': prod_code,
            'prod_limit': prod_limit,
            'new_balance': new_balance,
            'highest_balance': highest_balance
        }
        
        return redirect(url_for('predict'))

    return render_template('main.html')

# Predict based on collected data
@app.route('/predict')
def predict():
    # Retrieve data from session
    data = session.get('data', None)
    if data is None:
        return redirect(url_for('home'))

    # Prepare data for prediction
    prediction_data = np.array([[data['ovd_t1'], data['ovd_t2'], data['ovd_t3'],
                                 data['tovd_sum'], data['Pay_normal'], data['prod_code'],
                                 data['prod_limit'], data['new_balance'], data['highest_balance']]])

    # Make prediction
    my_prediction = model.predict(prediction_data)

    return render_template('result.html', prediction=my_prediction)

if __name__ == '__main__':
    app.secret_key = 'your_secret_key_here'
    app.run(debug=True)
