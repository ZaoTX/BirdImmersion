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
    IDList=[]
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
    curHeightList=[]
    # find header names
    idHeader=p.idHeaderName
    lngHeader = p.lngHeaderName
    latHeader = p.latHeaderName
    heightHeader = p.heightHeaderName
    timeHeader = p.timestampHeaderName
    for row in csv_reader:
        cur_id=row[idHeader]
        if ((last_id!=cur_id and last_id!='')):
            #collect information
            IDList.append(last_id)
            timeLists.append(curTimeList)
            heightLists.append(curHeightList)
            latLists.append(curLatList)
            lngLists.append(curLngList)
            curTimeList=[]
            curLatList=[]
            curLngList=[]
            curHeightList=[]
        else:
            curTimeList.append(row[timeHeader])
            curLatList.append(row[latHeader])
            curLngList.append(row[lngHeader])
            curHeightList.append(row[heightHeader])
        last_id=cur_id
    #store the information of the last individual
    IDList.append(last_id)
    timeLists.append(curTimeList)
    heightLists.append(curHeightList)
    latLists.append(curLatList)
    lngLists.append(curLngList)
    #after this process is done we can store them in d(Datasets)
    d.individuals=IDList
    d.TimeLists=timeLists
    d.heightLists=heightLists
    d.latLists=latLists
    d.lngLists=lngLists
#show information of this individual
def preAnalysis(idName,d,p):
    #find individual list
    
    #get the index of give individual
    ind=
    pass