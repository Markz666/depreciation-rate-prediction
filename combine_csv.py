# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 10:44:45 2017

@author: zmx
"""
import pandas as pd
import glob, os
 
os.chdir("C:/Users/zmx/Desktop/BIA 660/project")
#results = pd.DataFrame([])
merged = []
for file in glob.glob("clean_njauto_*"):
    namedf = pd.read_csv(file)
    merged.append(namedf)
results = pd.concat(merged)
results.to_csv('C:/Users/zmx/Desktop/BIA 660/project/combinedsuv.csv')
