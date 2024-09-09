# import essential libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline



# credit card fraud detection system

def fraud_prediction(obs):
    obs = preprocess(obs)
    result = np.where((boost.predict_proba(obs)[:, 1] >= 0.105263),1,0)
    if (result == 1):
        return "This is a fraudulent purchase!"
    else:
        return "This transaction is verified"

# check the results
fraud_prediction


# import shap library
import shap


def predict(*data):
      columns = ['distance_from_home', 'distance_from_last_transaction',
            'ratio_to_median_purchase_price', 'repeat_retailer', 'used_chip',
            'used_pin_number', 'online_order']
      df = pd.DataFrame([data], columns = columns)
      df = preprocess(df)
      prob_pred = boost.predict_proba(df)
      return {"Normal": float(prob_pred[0][0]), "Fraud": float(prob_pred[0][1])}

def interpret(*data):

      plt.style.use("fivethirtyeight")

      columns = ['distance_from_home', 'distance_from_last_transaction',
            'ratio_to_median_purchase_price', 'repeat_retailer', 'used_chip',
            'used_pin_number', 'online_order']
      df = pd.DataFrame([data], columns = columns)

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
