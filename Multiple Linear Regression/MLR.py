# -*- coding: utf-8 -*-
"""
Created on Wed May 22 15:34:22 2019

@author: bhara
"""
'''
Multiple linear regression - define the below 
1) Linearity 
2) homoscedasticity 
3) Multivariate normality 
4) Independence of errors
5) Lack of multicolinearity 
'''

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# switching the current working directory to the location where the py file and dataset exits
os.chdir('C:\\Users\\bhara\\PycharmProjects\\MachineLearning\\Multiple Linear Regression')

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
dataset.head()
X = dataset.iloc[:, :4].values
y = dataset.iloc[:, 4].values

# Encoding the categorical variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
label_encode_X = LabelEncoder()
X[:,3] = label_encode_X.fit_transform(X[:,3])

# Making the categorical variable to numeric value
onehotencoder = OneHotEncoder(categorical_features=[3])
X = onehotencoder.fit_transform(X).toarray()

# Creating the Dummy variables
# Be careful of the dummy variable trap
# due to multiple colinearity between the variables, model cannot differentiate between the variables
# removing the first column in the X variable.
X = X[:,1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, y, train_size=0.8,random_state=0)
train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling is not required for Multiple Linear regression
# library will take care of this.
# fitting linearregression to training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,Y_train)

# Predicting the Y^ from the test set
y_pred = regressor.predict(X_test)

# Building a model with backward elimination
import statsmodels.formula.api as sm
# the statsmodel doesn't have the X0 for the constant B0. need to add this
X = np.append(arr=np.ones((X.shape[0],1)),values=X,axis=1)



