# Credit-card-fraud-project-data-science


![fraud pic](https://github.com/user-attachments/assets/7cbc74b6-111e-4e46-a335-0011af95ba98)


AUTHOR: @aidahbaaniwanjirunjenga@gmail.com
Table of Contents
Business Problem
Data Source
Methods
Tech Stack
Quick glance at the Results
Lessons learned and Recommendation
Limitation and what can be Improved
Run Locally
Explore the notebook
Business Problem
Credit card frauds have always been a major concern for banking and financial institutions which result in unnecessary fees taken. Fraudster have several methods in achieving these unauthorized transactions and we wish to identify key components that help identify a fraudulent transaction. The idea is if we can correctly identify a fraudulent transaction we can stop the transaction from going through and save the money from being taken. In order to achieve this goal we need a policy that helps determine fraudulent transaction at the expense of not misclassifying a transaction as fraudulent which can also increase costs. We need an efficient system that balances the identification of normal and fraudulent transactions.

Data Source
My Google Drive
Methods
Exploratory Data Analysis
Multivariate Analysis
Visualizations
Modeling
App Deployment
Tech Stack
Python (Machine Learning Modeling and App preparation)
AWS S3 (Model Storage)
Gradio (Interface for app)
Hugging Face (App Deployment)
Quick Glance at the Results
Correlation Matrix between numeric features.



Confusion Matrix of XGBoost Classifier (Testing Set).



XGboost Feature Importance Plot.



Top 3 models on the testing set (with default parameters)

Model	Best Threshold	F1 Score	Accuracy	Recall	Precision
Logistic Regression	0.315789	79.48%	96.5%	76.67%	82.5%
Random Forest	0.315789	99.9%	99.9%	99.9%	100%
XGBoost	0.105263	99.9%	99.9%	99.9%	99.9%
Final Model used: XGBoost Classifier
Metric used: Recall, Precision, and Accuracy
What is the meaning behind the threshold?: The threshold is the probability set in order for us to classify a transaction as a fraudulent one. Therefore if the probability provided by our XGboost Classifier for being a fraudulent transaction was greater than 10.5%, then the transaction would be classified as a fraudulent one. This threshold was computed by checking random probabilities and picking the ones that returned the highest metrics when it came down to F1 score, accuracy, recall and precision. Remember we want to find a balance between correctly identifying fraudulent transaction and not misclassifying normal transaction as being fraud since this misidentification could cost a company a lot of money. Therefore, in terms of our metrics this means we want the best scores when it came down to only recall, precision, and accuracy. Where recall is the score that correctly identifies fraudulent transaction. Precision is the score in correctly identifying fraudulent transaction divided by the total number labelled as fraudulent transaction even the ones that weren't. Accuracy is the score of our model that correctly identifying the transactions correctly.
Lessons Learned and Recommendation
In this project I learned how to leverage feature importance using our Random Forest and Gradient Boosting models to determine what influences our response the most. Its important to note that some features might provide a negative influence to our response variable or a positive one. Since the goal for this project is to increase satisfactory level, we want to identify not only the top important features but also the ones that provide positive influence. For example, Cleanliness is a feature given and some logic would say as we decrease cleanliness so would satisfaction levels. This can also be said in reverse if we increase cleanliness then you would expect customers to be more satisfied with their experience, thus this feature provides a positive influence. A negative influence would say if we increase a feature then satisfaction level would decrease or vice-versa.
Limitation and what can be Improved
Note: Based on the feature importance plot we can see that ratio to median purchase price had one of the greatest influence in predicting a fraudulent transaction. Now the ratio is computed by taking the purchase price and dividing it by the median purchase price used on the card. Therefore, we must know the transaction price that fraudster performed, limiting the model from stopping the transaction before it even occurs. Also we must have a median purchase price on the card, but what if theres no history on the card. What do we use as the median purchase price for the card?
In order to improve our model we would require more attributes for our data. If you take a close look we are only using 7 predictors in order to determine our target/response of a fraudulent transaction. We can take more information on the card and the owner to determine more spending habits or calculate more probabilities that the transaction was in fact the owner.
Also in order to implement a system that stops a transaction before going through when the system believes it is a fraudulent one would require a whole new transactional system across all stores. Currently when you buy or receive a refund from a store, it may be instant to you but in the backend the process takes days. This leads to issues since we would want to stop transaction from going through therefore we would need some fast transactional system to achieve this. Just recently the U.S. government approved such systems which they have been testing since 2019, I believe it will go live this month in October 2024.
