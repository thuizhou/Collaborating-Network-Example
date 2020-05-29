#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np # linear algebra
from sklearn.model_selection import train_test_split #split dataset

np.random.seed(2020)

#the heteroscedastic gaussian error generated by chisq
err=np.random.normal(size=(2000,1))
sig=np.random.chisquare(1,size=(2000,1))

#the mean model generated by N(0,1)
mu=np.random.normal(size=(2000,1))
y=mu+err*sig

hetdata=np.c_[y,mu,sig]

#training
train,test=train_test_split(hetdata,test_size=0.4, random_state=2020)

#save dataset
np.save('train',train)
np.save('test',test)
