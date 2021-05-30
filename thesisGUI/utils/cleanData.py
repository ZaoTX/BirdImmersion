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
def interpolation(d,p,meth):
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
      df=df.interpolate(method =meth, limit_direction ='both',limit_area='inside')
      df=df.dropna()
      df.to_csv(outpath+'/'+meth+'_interporlation.csv',index=False)

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
# compute DBSCAN algorithm for each individual to detect the outlier              
def Clustering(d,p,eps):
    import numpy as np
    from sklearn.cluster import DBSCAN
    sizeOfoutput=0
    totalLines=0
    outputLines=np.empty(0)
    outputList=[]
    for i in range(0,len(d.timeLists)):
        latList=d.latLists[i]
        lngList=d.lngLists[i]
        heightList=d.heightLists[i]
        # stack the lists
        position_X=np.column_stack((latList, lngList,heightList))
        position_X = position_X.astype(np.float64)
        clustering = DBSCAN(eps=eps, min_samples=2).fit(position_X)
        labels = clustering.labels_
        
        #index of -1(outliers)
        outlierIndex= np.where(labels==-1)[0]
        outlierIndexList=outlierIndex.tolist()
        outputList.append(outlierIndexList)
        
        sizeOfoutput=sizeOfoutput+len(outlierIndex)
        outlierIndex = outlierIndex+totalLines
        outputLines = np.concatenate((outputLines,outlierIndex))
        totalLines=len(labels)
    return outputLines,outputList
        