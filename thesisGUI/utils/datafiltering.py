# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 20:56:23 2020

@author: heziy
"""
import pandas as pd
import os
def filtering(headers,d):
      dataFrame=pd.read_csv(d.filepath)
      #find the columns we want to drop
      import numpy as np
      droplist = np.setdiff1d(d.headers,headers)
      workdir=d.workdir
      path=workdir+'/filtered.csv'
      print(path)
      for col in droplist:
            dataFrame.drop(col, axis = 1, inplace = True)
      dataFrame.to_csv(path, index = False)
      
            
            