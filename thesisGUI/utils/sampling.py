# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 20:25:52 2020

@author: ZiyaoHe
"""
import os
import csv
'''
 from the first row of the same individual, 
 it takes for each n line and store into new csv
'''
def averageSampling(d,p,n):
      
    #d:launch.d, p: launch.pSetups, n: sample for each n points
    base_dir = d.workdir
    filePath = d.filepath
    outpath = base_dir+'/'+'sample'# define the output folder
    if not os.path.exists(outpath):
            os.makedirs(outpath)
    csv_file=open(filePath, encoding='utf-8')
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    fieldnames = csv_reader.fieldnames
    count=0
    last_id=''
    idHeader=p.idHeaderName
    
    csvfile_write = open(outpath+'/'+'average_sample.csv', 'a', newline='')
    writer = csv.DictWriter(csvfile_write
                                    ,fieldnames=fieldnames
                                    )
    writer.writeheader()
    for row in csv_reader:
        cur_id=row[idHeader]
        if last_id!=cur_id:
             count=1
             writer.writerow(row)
        else:
            # the sample individual
            count=count+1
            if((count-1)%n==0):
                writer.writerow(row)
            
        last_id=cur_id
'''
Douglas peucker sampling:
  1.Find the first point A and last point B of the whole trajectory 
  2.Find the furtherst point C to line AB on the trajectory
  3.If the furtherst distance is less than our threshold then we use AB to represent the trajectory
    Else Do the same thing to line AC and BC
  O(n^2)
'''
def Douglas(d,p,epsilon):
    import math
    def d_2points(lat1,lng1,h1,lat2,lng2,h2):
        R = 6373.0 #radius of earth
        
        dlng = lng1-lng2
        dlat = lat1 - lat2
        dh= h1-h2 
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlng / 2)**2

        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c
        dis =math.sqrt( dh**2+distance**2)
        return dis
    
    def d_pointLine(lat1,lng1,h1,lat2,lng2,h2,lat3,lng3,h3):
     
    	a=d_2points(lat1,lng1,h1,lat2,lng2,h2)
    	b=d_2points(lat3,lng3,h3,lat2,lng2,h2)
    	c=d_2points(lat1,lng1,h1,lat3,lng3,h3)
    	s=(a+b+c)/2    
    	A=math.sqrt(s*(s-a)*(s-b)*(s-c))  #Heron's formula
    	return 2*A/a;# area of triangle ABC= 0.5*h*|AB| h= 2A/a  
    base_dir = d.workdir
    filePath = d.filepath
    outpath = base_dir+'/'+'sample'# define the output folder
    if not os.path.exists(outpath):
            os.makedirs(outpath)
    csv_file=open(filePath, encoding='utf-8')
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    fieldnames = csv_reader.fieldnames
    #initialize
    last_id=''
    currentLngList=[]
    currentLatList=[]
    currentHeightList=[]
    # find header names
    idHeader=p.idHeaderName
    lngHeader = p.lngHeaderName
    latHeader = p.latHeaderName
    heightHeader = p.heightHeaderName
    csvfile_write = open(outpath+'/'+'douglas_sample.csv', 'a', newline='')
    writer = csv.DictWriter(csvfile_write
                                    ,fieldnames=fieldnames
                                    )
    writer.writeheader()
    for row in csv_reader:
        cur_id=row[idHeader]
        if (last_id!=cur_id and last_id!=''):
             count=1
             writer.writerow(row)
        else:
            # the sample individual
            count=count+1
            if((count-1)%n==0):
                writer.writerow(row)
            
        last_id=cur_id
    


    