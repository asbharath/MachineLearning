#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 21:25:19 2019

@author: aazur3e
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,1].values

# splitting the dataset into training set and test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,train_size=1/3,random_state = 0)

# fitting the SLR to the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

# fits the regressor object to the fit the x train and the y train
regressor.fit(x_train,y_train)
# y_train is the dependent variable  and x_train is the independent variable
# correlation are learnt from the training test and can now be applied to the test set.

# predecting the test set
y_pred = regressor.predict(x_test)

# visualising the training set results
plt.scatter(x_train,y_train,color='red')
plt.plot(x_train,regressor.predict(x_train),color='blue') # regression line
plt.title('salary vs experience(training set)')
plt.xlabel('Years of experience')
plt.ylabel('salary')
plt.show()

# visualising the test set results
plt.scatter(x_test,y_test,color='red')
plt.plot(x_train,regressor.predict(x_train),color='blue') # regression line
plt.title('salary vs experience (test set results)')
plt.xlabel('Years of experience')
plt.ylabel('salary')
plt.show()