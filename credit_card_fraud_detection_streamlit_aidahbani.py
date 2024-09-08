
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Credit Card Fraud Detection System")

# File uploader for user to upload the dataset
uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

if uploaded_file is not None:
    # Load the data
    card = pd.read_csv(uploaded_file)
    
    # Display basic information
    st.write("## Data Preview")
    st.write(card.head())
    
    # Data dimensions
    st.write("### Data Dimensions")
    st.write(card.shape)
    
    # Column names
    st.write("### Column Names")
    st.write(card.columns)
    
    # Column information
    st.write("### Column Information")
    st.write(card.info())
    
    # Summary statistics
    st.write("### Summary Statistics")
    st.write(card.describe().T)
    
    # Check for missing values
    st.write("### Missing Values")
    st.write(card.isna().sum())
    
    # Visualizations
    st.write("## Visualizations")
    
    # Correlation heatmap
    cor = card.corr()
    fig, ax = plt.subplots()
    sns.heatmap(cor, annot=True, fmt='.2f', cmap='crest', linewidth=0.7, ax=ax)
    plt.title("Correlation Matrix")
    st.pyplot(fig)
else:
    st.write("Please upload a CSV file to get started.")
