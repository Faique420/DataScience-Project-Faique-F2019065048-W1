
!pip install flask-ngrok

!pip install flask-waitress

!ls

!ngrok config add-authtoken 2C8HYH9xXDD8PXyZJfwj9Y8t5ER_iZGtSXT5cHXz4u7qUq42

# in ngrok.yml
!authtoken: 2C8HYH9xXDD8PXyZJfwj9Y8t5ER_iZGtSXT5cHXz4u7qUq42

!ngrok http 80

#!/usr/bin/env python
# coding: utf-8

# In[9]:

from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import joblib
import pickle

app = Flask(__name__, template_folder = 'template')

model = joblib.load(open('Pakistan_temperature_predictor_model.pkl', 'rb'))

mydata = pd.read_csv(r'tempreture_1901_2016_pakistan.csv')
df = pd.DataFrame(mydata, columns = ['Temperature - (Celsius)','Year','Month'])

# In[11]:

app = Flask(__name__, template_folder = 'template')

@app.route('/')
def home():
    return render_template('temperature.html')
@app.route('/', methods=['POST'])
def predict():
    a = np.array(df['Month'], df['Year'])
    b = np.array(df['Temperature - (Celsius)'].values.tolist())
    data1 = request.form['a']
    data2 = request.form['b']
    arr = np.array([[data1, data2]])
    pred = model.predict(arr)
    
    
    #If the output is negative, the values entered are unreasonable to the context of the application
    #If the output is greater than 0, return prediction
    if pred < 0:
        return render_template('temperature.html', prediction_text = "Prediction is negative, values entered are not correct")
    elif pred >= 0:
        return render_template('temperature.html', prediction_text = 'Predicted Temperature is: ${}'.format(pred))

if __name__ == "__main__":
    from waitress import serve
    #serve(app, host="0.0.0.0", port=8080)
    app.debug==True;
    app.run()