# import essential libraries
import shap
import pickle
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import tempfile
import os 
import boto3 
# from pathlib import Path


# load our models 
load_dotenv()
client = boto3.client('s3', aws_access_key_id = os.getenv('aws_access_key'),aws_secret_access_key=os.getenv('aws_secret_key'))
bucket_name = "credit-card-fraud-app"
key = "boost.sav"

with tempfile.TemporaryFile() as fp:
    client.download_fileobj(Fileobj=fp, Bucket=bucket_name, Key=key)
    fp.seek(0)
    boost = pickle.load(fp)

# boost_path = Path(__file__).parents[0] / "Models/boost.sav"
# boost = pickle.load(open(boost_path,"rb"))

# functions

# preprocessing data function
def preprocess(data):
    columns = ['distance_from_home', 'distance_from_last_transaction',
                'ratio_to_median_purchase_price', 'repeat_retailer', 'used_chip',
                'used_pin_number', 'online_order']
    
    df = pd.DataFrame([data], columns = columns)
    
    # convert data type
    df[['repeat_retailer','used_chip','used_pin_number','online_order']] = df[['repeat_retailer','used_chip','used_pin_number','online_order']].astype('int')
    
    return df


# Prediction function with probabilities
def predict(*data):
        df = preprocess(data)
        prob_pred = boost.predict_proba(df)
        return {"Normal": float(prob_pred[0][0]), "Fraud": float(prob_pred[0][1])}

# plot function
def interpret(*data):
        plt.style.use("fivethirtyeight")
        
        df = preprocess(data)
        
        explainer = shap.TreeExplainer(boost)
        shap_values = explainer.shap_values(df)
        scores_desc = list(zip(shap_values[0], df.columns))
        scores_desc = sorted(scores_desc)
        fig_m = plt.figure(tight_layout=True)
        plt.barh([s[1] for s in scores_desc], [s[0] for s in scores_desc])
        plt.title("Feature Shap Values")
        plt.ylabel("Shap Value")
        plt.xlabel("Feature Importance")
        plt.tight_layout()
        
        return fig_m
    
    
    

import streamlit as st

st.title("Credit Card Fraud Prediction System")
st.write("""
This is a Web App that predicts whether a credit card transaction is fraudulent or not. Just input the following parameters and click the predict button. If you want to see the influence that each parameter had on the outcome, click the explain button.
""")

# Input parameters
repeated_retailer = st.radio("Repeat Retailer", ["No", "Yes"], index=0, help="Was the transaction at a repeated store?")
online_order = st.radio("Online Order", ["No", "Yes"], index=0, help="Was the transaction an online order?")
used_chip = st.radio("Used Chip", ["No", "Yes"], index=0, help="Did the purchase use the security chip of the card?")
used_pin = st.radio("Used Pin Number", ["No", "Yes"], index=0, help="Did the transaction use the pin code of the card?")
distance_home = st.number_input("Distance From Home (miles)", value=25, help="How far was the transaction from the card owner's house? (in miles)")
distance_last = st.number_input("Distance From Last Transaction (miles)", value=5, help="How far away was it from the last transaction that happened? (in miles)")
ratio_median = st.number_input("Ratio Median Purchase Price", value=1.8, help="Divide the purchase price by card owner's median purchase price")

# Prediction and Explanation buttons
predict_btn = st.button("Predict")
interpret_btn = st.button("Explain")

# Dummy prediction and interpretation functions
def predict(inputs):
    # Replace with your model's prediction code
    return "Fraudulent" if sum(inputs) > 50 else "Not Fraudulent"

def interpret(inputs):
    # Replace with your model's interpretation code
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.bar(["Distance Home", "Distance Last", "Ratio Median"], inputs[:3])
    return fig

# Handling button clicks
if predict_btn:
    inputs = [distance_home, distance_last, ratio_median, repeated_retailer, used_chip, used_pin, online_order]
    inputs = [float(val) if isinstance(val, (int, float)) else 1 if val == "Yes" else 0 for val in inputs]
    prediction = predict(inputs)
    st.subheader("Prediction")
    st.write(prediction)

if interpret_btn:
    inputs = [distance_home, distance_last, ratio_median, repeated_retailer, used_chip, used_pin, online_order]
    inputs = [float(val) if isinstance(val, (int, float)) else 1 if val == "Yes" else 0 for val in inputs]
    fig = interpret(inputs)
    st.subheader("Interpretation")
    st.pyplot(fig)

"""Running on Url http://localhost:8501

"""

