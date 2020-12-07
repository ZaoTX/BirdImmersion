# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 20:40:34 2020

@author: ZiyaoHe
"""

#split for each individual to get different IDs
#return different ids and it's coordinates
def getIndividualNum(d,p):
    import csv
    #outputs: lists of list for each individual
    timeLists=[]
    heightLists=[]
    latLists=[]
    lngLists=[]
    filePath = d.filepath
    #base_dir+'/'+'filtered.csv'
    csv_file=open(filePath, encoding='utf-8')
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    #create initial list for each individual
    cur_id=''
    last_id=''
    curTimeList=[]
    curLatList=[]
    curLngList=[]
    curHeight=[]
    for row in csv_reader:
        cur_id=row[idHeader]
        if ((last_id!=cur_id and last_id!='')or (next(csv_reader)=='')):
            #collect information
        else:
      