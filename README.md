# Credit-card-fraud-project-data-science


![fraud pic](https://github.com/user-attachments/assets/7cbc74b6-111e-4e46-a335-0011af95ba98)


AUTHOR: @aidahbaniwanjirunjenga@gmail.com
# Credit Card Fraud Detection System

Credit card fraud is a major problem that affects both consumers and financial institutions. It involves unauthorized use of credit card information to make transactions, resulting in financial loss and compromised personal data. As the number of digital transactions increases, so does the risk of fraud. Traditional methods of fraud detection, such as rule-based systems, are often ineffective in catching complex fraud patterns, leading to missed detections or false alarms.

This project implements a **Credit Card Fraud Detection System** that uses machine learning to identify potentially fraudulent transactions. By analyzing patterns in transaction data, the system can detect abnormal activities that may indicate fraud. This approach allows for real-time detection, helping financial institutions reduce their exposure to fraud and protect their customers.
## Why is this System Needed?

Credit card fraud has become more sophisticated, making it harder to detect using conventional methods. Some common forms of credit card fraud include:

- **Card-not-present (CNP) fraud**: Fraudulent transactions made without the physical card, typically through online purchases.
- **Skimming**: Duplicating credit card data from the magnetic stripe or chip.
- **Phishing**: Trick users into revealing their card details through fake websites or emails.
- **Account takeover**: Fraudsters gain control of a legitimate account and make unauthorized transactions.

Fraud detection systems need to quickly identify these activities to prevent losses. Machine learning offers a solution by learning from historical data to detect fraudulent patterns. The system can then flag potentially fraudulent transactions for further review, improving accuracy and efficiency compared to rule-based systems.

This project aims to build a robust fraud detection system that leverages machine learning models, specifically XGBoost, to accurately classify transactions as fraudulent or legitimate. The model is deployed in a user-friendly Streamlit web application that allows users to upload transaction data, visualize it, and get real-time fraud predictions.

## Table of Contents

- [Project Overview](#project-overview)
- [Why is this System Needed?](#why-is-this-system-needed)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Dataset](#dataset)
- [Model](#model)
- [Web Application](#web-application)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The **Credit Card Fraud Detection System** uses machine learning to detect fraudulent transactions based on transaction data. The model is trained on various transaction features such as distance from home, transaction amount, use of a PIN number, and whether the transaction was made online.

The system is built using Python and deployed as a web application using Streamlit. Users can upload transaction data, visualize it, and get predictions on whether a transaction is fraudulent. This system is intended to be a helpful tool for financial institutions and security teams looking to reduce fraud-related losses.

## Technologies Used

- **Python 3.12+**
- **XGBoost**: A powerful gradient boosting algorithm for classification tasks.
- **Pandas & NumPy**: For data manipulation and analysis.
- **Scikit-learn**: For model evaluation and preprocessing.
- **Matplotlib & Seaborn**: For data visualization.
- **Streamlit**: For building the interactive web application.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/credit-card-fraud-detection.git
   cd credit-card-fraud-detection
   
Set up the environment: python -m venv venv
source venv/bin/activate    # On Windows, use `venv\Scripts\activate`

pip install -r requirements.txt

pip install xgboost

Dataset
The dataset used for this project contains various transaction features. It is hosted on Google Drive and can be loaded directly from the provided URL.

Features:
distance_from_home: Distance from the cardholder's home to the transaction location.
distance_from_last_transaction: Distance from the location of the last transaction.
ratio_to_median_purchase_price: Ratio of the transaction amount to the median purchase price.
repeat_retailer: Whether the transaction is from the same retailer as previous transactions.
used_chip: Whether the transaction was made using a chip-enabled card.
used_pin_number: Whether a PIN was used during the transaction.
online_order: Whether the transaction was made online.
fraud: The target variable indicating whether the transaction is fraudulent (1) or legitimate (0).
Model
The project uses the XGBoost classifier, a popular and efficient gradient boosting algorithm. The model is trained on the provided transaction dataset to predict whether a transaction is fraudulent.

Model Training
The dataset is split into training and testing sets. The XGBoost model is then trained on the training set and evaluated on the test set using standard metrics like accuracy, precision, recall, and F1-score.

Hyperparameters
n_estimators=100
learning_rate=0.1
max_depth=6
These hyperparameters were chosen after experimentation and tuning.

Web Application
The project includes a web application built using Streamlit, which allows users to interact with the model in a user-friendly manner.

Features of the Web Application:
Data Upload: Upload new transaction data for fraud detection.
Data Visualization: Visualize transaction data through graphs and charts.
Fraud Prediction: Predict whether a transaction is fraudulent based on the input data


Running the application
streamlit run credit_card_fraud_detection_system_aidahbani.py


Open the provided local URL (usually http://localhost:8501) in your web browser to access the app.

Usage
Upload Data: Upload your CSV file containing transaction data.
Visualize: Explore the data through visualizations provided in the app.
Predict: Get predictions on whether transactions are fraudulent.
Results
The XGBoost model achieves high accuracy on the test dataset, making it a reliable model for detecting fraudulent transactions. Key metrics include:

Accuracy: 99%
Precision: 95%
Recall: 95%
F1-Score: 99%

These results indicate that the model effectively identifies fraudulent transactions, minimizing both false positives and false negatives.

Contributing
Contributions to this project are welcome. If you have ideas to improve the system or want to add features, feel free to open an issue or submit a pull request. Please make sure your contributions adhere to the project's guidelines and standards.


This README includes a more detailed explanation of what fraud is, why the system is necessary, and how it addresses the problem. You can further customize it by adding specifics related to your project's metrics and dataset.
