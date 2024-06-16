from flask import Flask , request,render_template
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import RobustScaler
from sklearn import metrics
import joblib 


ML_columns_initial_test = ['Fe', 'Mn', 'Si', 'Ms']

# Read the original CSV file
original_data = pd.read_csv("/home/abrar/fe_mn_si_alloy_gcp_cloud_run_deploy/matrix_Fe-Mn-Si.csv")

selected_data_new = original_data[ML_columns_initial_test]
# Remove rows with NaN values
selected_data_new = selected_data_new.dropna()
# Separate the features and the target variable
X = selected_data_new.drop(columns=['Ms'])  # Features
y = selected_data_new['Ms']  # Target variable

# Apply Robust Scaling to the entire dataset
scaler = RobustScaler()
X = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

# Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)


# Save the trained model using joblib

joblib.dump(model, 'linear_regression_model.joblib')
joblib.dump(scaler, 'scaler.joblib')

