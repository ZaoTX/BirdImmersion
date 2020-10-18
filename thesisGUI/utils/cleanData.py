# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 20:52:58 2020

Clean data: Mainly deal with missing value problem
@author: heziy
"""
import os
import pandas as pd
#interpolation of missing value in location information, better performance in high resolution dataset
# pandas interpolate() https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.interpolate.html
def interpolation(d,p):
      base_dir = d.workdir
      #specify the critical headers
#      latHeader=p.latHeaderName
#      lngHeader=p.lngHeaderName
#      heightHeader=p.heightHeaderName
      filePath = d.filepath
      outpath = base_dir+'/'+'clean'
      if not os.path.exists(outpath):
               os.makedirs(outpath)
      #csv_file=open(filePath, encoding='utf-8')
      df = pd.read_csv(filePath)#get dataframe
      df=df.interpolate(method ='linear', limit_direction ='forward',limit_area='inside')
      df.to_csv(outpath+'/'+'linearInterporlation.csv',index=False)

# pandas dropna(): https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html
def removeMissing(d,p):
      base_dir = d.workdir
      #specify the critical headers
#      latHeader=p.latHeaderName
#      lngHeader=p.lngHeaderName
#      heightHeader=p.heightHeaderName
      filePath = d.filepath
      outpath = base_dir+'/'+'clean'
      if not os.path.exists(outpath):
               os.makedirs(outpath)
      #csv_file=open(filePath, encoding='utf-8')
      df = pd.read_csv(filePath)#get dataframe
      df=df.dropna()
      df.to_csv(outpath+'/'+'removeMissing.csv',index=False)
                  
                  
                  
                  
            
      