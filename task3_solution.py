# -*- coding: utf-8 -*-
"""
Created on Fri May  8 17:28:59 2020

@author: Toby
"""


import pandas as pd


# import data  -> dataframe
names = pd.read_csv('task3_names.6020a082.txt', header=None)        #row with names
salaries = pd.read_csv('task3_salary.c693064e.txt', header=None)    #row with salaries

combined = pd.concat([names, salaries], axis=0, ignore_index=True)  #merge the two rows together

combined.columns = combined.iloc[0]                 #replaxe column index with names
combined_clean = combined.drop(combined.index[0])   #remove name row

list = combined_clean.groupby(combined_clean.columns, axis=1).sum() #add same column names together

sorted_list = list.sort_values(1, axis=1, ascending=False)

# -> highest amount for "Charlotte de Berry"