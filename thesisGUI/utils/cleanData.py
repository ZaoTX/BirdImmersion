# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 20:52:58 2020

@author: heziy
"""
import os
import pandas as pd
#interpolation of missing value in location information
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
      df.to_csv(outpath+'/'+'linearInterporlation.csv')
#      csv_reader = csv.DictReader(csv_file, delimiter=',')
#      fieldnames = p.choosenHeaders
#      lastRow = None
#      for row in csv_reader:
#            #find the first row without any missing value
#            if(lastRow==None):#initial
#                  #check if there is missing value
#                  lat=row[latHeader]
#                  lng=row[lngHeader]
#                  height=row[heightHeader]
#                  if(lat,lng,height in (None, "")):
#                        break
#                  else:
#                        lastRow=row
#            else:
#                  lat=row[latHeader]
#                  lng=row[lngHeader]
#                  height=row[heightHeader]
#                  nextrow=next(csv_reader)
#                  nextlat=nextrow[latHeader]
#                  nextlng=nextrow[lngHeader]
#                  nextheight=nextrow[heightHeader]
                  
                  
                  
                  
            
      