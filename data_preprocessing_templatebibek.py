# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 14:08:36 2018

@author: bs
"""
#data preprocessing template
# importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing dataset
dataset= pd.read_csv("Data.csv")
 X= dataset.iloc[:,:-1].values
 y= dataset.iloc[:,3].values
 
 
 #splitting datasets into training and test set
 from sklearn.model_selection import train_test_split
 X_train,y_train,X_test,y_test= train_test_split(X,y,test_size=0.2,random_state=0)
 
 """ #feature scaling
 from sklearn.preprocessing import StandardScaler
 sc_X= StandardScaler()
 X_train=sc_X.fit_transform(X_train)
 X_test= sc_X.transform(X_test)"""