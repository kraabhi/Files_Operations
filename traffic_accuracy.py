#!/usr/bin/env python
# coding: utf-8

# In[200]:


import pandas as pd
import json
import csv
import numpy as np
import os
from sklearn.metrics import accuracy_score

# first_arg =pd.read_csv("Cax_Traffic_Solution_file.csv")
# second_arg =pd.read_csv("Book4.csv")

first_arg = pd.read_csv(sys.argv[1])
second_arg = pd.read_csv(sys.argv[2])

mer_all = pd.merge(first_arg, second_arg, on="id")
mer_all = mer_all.fillna(0)

public = mer_all[mer_all["Label"] == "Public"]
private = mer_all[mer_all["Label"] == "Private"]

# Public score

s1 = public[["id", "Label"]]

df_pub1 = public.filter(regex='_x')
result1_pub = pd.concat([s1, df_pub1], axis=1)
drop_col =["id" , "Label"]
result_pub1 = result1_pub.drop(drop_col , axis = 1)

df_pub2 = public.filter(regex='_y')
result2_pub = pd.concat([s1, df_pub2], axis=1)
result_pub2 = result2_pub.drop(drop_col , axis = 1)

accuracy_pb = []
for i in range(0, 1067):
    y_true = result_pub1.loc[i]
    y_pred = result_pub2.loc[i]
    acc_pub = accuracy_score(y_true, y_pred) * 100
    accuracy_pb.append(acc_pub)
    
pb_score = sum(accuracy_pb)/len(public)

public_df = pd.DataFrame({'x': [pb_score]})



# Private score 

s2 = private[["id", "Label"]]

df_private1 = private.filter(regex='_x')
result1_private = pd.concat([s2, df_private1], axis=1)
drop_col =["id" , "Label"]
result_private1 = result1_private.drop(drop_col , axis = 1)

df_private2 = private.filter(regex='_y')
result2_private = pd.concat([s2, df_private2], axis=1)
result_private2 = result2_private.drop(drop_col , axis = 1)

accuracy_private = []
for i in range(1067, 2667):
    y_true = result_private1.loc[i]
    y_pred = result_private2.loc[i]
    acc_private = accuracy_score(y_true, y_pred) * 100
    accuracy_private.append(acc_private)
    
pr_score = sum(accuracy_private)/len(private)

private_df = pd.DataFrame({'x': [pr_score]})


private_df.to_csv(sys.argv[3], index=False)
public_df.to_csv(sys.argv[4], index=False)

