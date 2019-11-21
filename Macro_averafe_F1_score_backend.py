#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import sys
from sklearn.metrics import f1_score

# first_arg =pd.read_csv("C:/Users/admin/Documents/Cax/contest_mortage/Contest_Mortgage/CAX_SolutionFile.csv")
# second_arg =pd.read_csv("C:/Users/admin/Desktop/practice_problems/mortgage_new/full.csv")

first_arg =pd.read_csv(sys.arg[1])
second_arg =pd.read_csv(sys.arg[2])

mer_all =pd.merge(first_arg, second_arg, on = "Unique_ID")
mer_all.head()

mer_all['Result_Predicted_x']=mer_all['Result_Predicted_x'].map({'NOT FUNDED': 0,'FUNDED':1} ) 
mer_all['Result_Predicted_y']=mer_all['Result_Predicted_y'].map({'NOT FUNDED': 0,'FUNDED':1} ) 

public = mer_all[mer_all["Label"]=="public"]
private = mer_all[mer_all["Label"]=="private"]

# public F1 score

public_predicted = public["Result_Predicted_y"]
public_actual = public["Result_Predicted_x"]
pb_score = f1_score(public_actual ,public_predicted,average='macro')
public_score =pd.DataFrame({'x' : [pb_score]})

#public_score.to_csv('pub_score.csv',index = False)
public_score.to_csv(sys.argv[4],index = False)
#public_score

# private F1 score

private_predicted = private["Result_Predicted_y"]
private_actual = private["Result_Predicted_x"]
pri_score = f1_score(private_actual ,private_predicted,average='macro')
private_score =pd.DataFrame({'x' : [pri_score]})

#private_score.to_csv('pri_score.csv',index = False)
private_score.to_csv(sys.argv[3],index = False)
#private_score

