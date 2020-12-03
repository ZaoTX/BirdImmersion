# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 20:56:23 2020

@author: heziy
"""
import pandas as pd

def filtering(headers,d):
      dataFrame=pd.read_csv(d.filepath)
      #find the columns we want to drop
      import numpy as np
      droplist = np.setdiff1d(d.headers,headers)
      workdir=d.workdir
      path=workdir+'/filtered.csv'
      
      for col in droplist:
            #print(col)
            dataFrame.drop(columns=[col], axis = 1, inplace = True)
      dataFrame.to_csv(path, index = False, header=True)
      print(path)
            
            