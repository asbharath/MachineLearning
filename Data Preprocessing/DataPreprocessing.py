#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 19:53:01 2019

@author: aazur3e
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing the data set 
dataset = pd.read_csv('Data.csv')


#importing all the rows and all the column but the last one
x = dataset.iloc[:,:-1].values

#importing all the rows and only the column 3. 
y = dataset.iloc[:,3].values

#missing data
# 1) can remove the line - but will miss crucial data
# 2) better option is to take the mean

#taking the mean 
from sklearn.impute import SimpleImputer
#imputer is imported to compute the mean
imputer = SimpleImputer(missing_values=np.nan,strategy='mean')
#imputer object needs to be fitted to the matrix x
imputer = imputer.fit(x[:,1:3])
#need to take the mean
x[:,1:3] = imputer.transform(x[:,1:3])

#Encoding the categorical variable 
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_country = LabelEncoder()
x[:,0] = labelencoder_country.fit_transform(x[:,0])
onehotencoder = OneHotEncoder(categories=None)
x = onehotencoder.fit_transform(x).toarray()

labelencoder_x = LabelEncoder()
y = labelencoder_x.fit_transform(y)

#splitting the data set into training set and test set
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 0)
#y train is y part of the dependent variable vector associated to x train 

#Feature scaling - Need to transform the variables to scale to one another 
#reason being the euclidean distance between the 2 points will be large
#there are chances the model might ignore the smaller value 
#sometimes the machine learning model are not based on eucledian distances
#(eg: decision trees)
#its good to do feature scaling so that the algorithm converge much faster
#else it will run for a longer time


from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
#why for train set we need to fit and transform and not the case for test set?
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)

#dummy variables - do we need to scale? it depends on the context.
# it will be good to scale and it will be good for predection, but we will lose the
#intrepretation of the variables.
#classification problem with categorical dependent variable
