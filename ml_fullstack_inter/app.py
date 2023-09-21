# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np
import tensorflow as tf
import joblib


# Load the Random Forest CLassifier model
filename = "model2.pkl"
model = joblib.load(filename)

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

my_prediction = None

@app.route('/feature-page.html', methods=['GET','POST'])
def feature():
    if request.method == 'POST':
        id = float(request.form['id'])
        ovd_t1 = float(request.form['ovd_t1'])
        ovd_t2 = float(request.form('ovd_t2'))
        ovd_t3 = float(request.form('ovd_t3'))
        tovd_sum = float(request.form['ovd_sum'])
        Pay_normal = float(request.form['Pay_normal'])
        prod_code = float(request.form('prod_code'))
        prod_limit = float(request.form['prod_limit'])
        new_balance = float(request.form['new_balance'])
        highest_balance = float(request.form('highest_balance'))
        
        data = np.array([[id, ovd_t1, ovd_t2, ovd_t3, tovd_sum, Pay_normal, prod_code, prod_limit, new_balance, highest_balance]])
        my_prediction = model.predict(data)
        
        return render_template('result.html', prediction=my_prediction)
    return render_template('feature-page.html')
@app.route('/process-feature', methods=['POST'])
def process_feature():
    if request.method == 'POST':
        fea_1 = float(request.form['fea_1'])
        fea_2 = float(request.form('fea_2'))
        fea_3 = float(request.form('fea_3'))
        fea_4 = float(request.form['fea_4'])
        fea_5 = float(request.form['fea_5'])
        fea_6 = float(request.form('fea_6'))
        fea_7 = float(request.form['fea_7'])
        fea_8 = float(request.form['fea_8'])
        fea_9 = float(request.form('fea_9'))
        fea_10 = float(request.form['fea_10'])
        fea_11 = float(request.form('fea_11'))         
        
        

if __name__ == '__main__':
	app.run(debug=True)

