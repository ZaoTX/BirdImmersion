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
            if(heightHeader=='------'):
                curHeightList.append(0)
                # the add the information into list
                curLngList.append(row[lngHeader])
                curLatList.append(row[latHeader])
                curTimeList.append(row[timeHeader])
            else:   
                curHeightList.append(row[heightHeader])
                # the add the information into list
                curLngList.append(row[lngHeader])
                curLatList.append(row[latHeader])
                curTimeList.append(row[timeHeader])
            
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
def preAnalysis(idName,d,iB):
    #find individual list
    IDList=d.individuals
    timeLists=d.TimeLists
    heightLists=d.heightLists
    latLists=d.latLists
    lngLists=d.lngLists
    #get the index of give individual
    ind=IDList.index(idName)
    timeList=timeLists[ind]
    heightList=heightLists[ind]
    latList=latLists[ind]
    lngList=lngLists[ind]
    #get the whole number of datapoints
    iB.setDataPoints(len(timeList))
    #get the number of rows with missing values
    missingHeight=heightList.count('')
    missingLat=latList.count('')
    missingLng=lngList.count('')
    num_Missing=max(missingHeight,missingLat,missingLng)
    iB.setMissing(num_Missing)
    #get start lat lng height
    #get the first non-empty value of the list
    Lats=list(filter(lambda a: a != '', latList))
    Lngs=list(filter(lambda a: a != '', lngList))
    Heights=list(filter(lambda a: a != '', heightList))
    s_lat=''
    s_height=''
    s_lng=''
    e_lat=''
    e_lng=''
    e_height=''
    
    
    slat_id=0
    slng_id=0
    sh_id=0
    elat_id=0
    elng_id=0
    eh_id=0
    if(len(Lats)!=0):
          s_lat=Lats[0]
          e_lat=Lats[-1]
          slat_id=latList.index(s_lat)
          elat_id=latList.index(e_lat)
    if(len(Lngs)!=0):
          s_lng=Lngs[0]
          e_lng=Lngs[-1]
          slng_id=lngList.index(s_lng)
          elng_id=lngList.index(e_lng)
    if(len(Heights)!=0):
          s_height=Heights[0]
          e_height=Heights[-1]
          sh_id=heightList.index(s_height)
          eh_id=heightList.index(e_height)
    #get max of start id
    start_id=max(slat_id,slng_id,sh_id)
    end_id=max(elat_id,elng_id,eh_id)
    startPos='(lat={0},lng={1},height={2})'.format(s_lat,s_lng,s_height)
    endPos='(lat={0},lng={1},height={2})'.format(e_lat,e_lng,e_height)
    #set start and end pos
    iB.setStartPos(startPos)
    iB.setEndPos(endPos)
    #get Start and end timestamp
    startTime=timeList[start_id]
    endTime=timeList[end_id]
    iB.setStartTime(startTime)
    iB.setEndTime(endTime)
def PostAnalysis(idName,d,iB):
    #get information of sampled results
    getPostInfo(iB)
    #find orignial individual list
    IDList=d.individuals
    timeLists=d.TimeLists
#    heightLists=d.heightLists
#    latLists=d.latLists
#    lngLists=d.lngLists
    #find sampled dataset
    post_timeLists=iB.timeLists
    post_heightLists=iB.heightLists
    post_latLists=iB.latLists
    post_lngLists=iB.lngLists
    #get the index of give individual
    ind=IDList.index(idName)
    #orignial data
    ind=IDList.index(idName)
    timeList=timeLists[ind]
#    heightList=heightLists[ind]
#    latList=latLists[ind]
#    lngList=lngLists[ind]
    #result of this individual
    post_timeList=post_timeLists[ind]
    post_heightList=post_heightLists[ind]
    post_latList=post_latLists[ind]
    post_lngList=post_lngLists[ind]
    #calculate compression ratio
    wholeNumber=len(timeList)
    #record compression ratio
    iB.compressionratio=(1-len(post_timeList)/wholeNumber)*100
    pass
#store the Lists in infoBuffer
def getPostInfo(iB):
    import csv
    timeLists=[]
    heightLists=[]
    latLists=[]
    lngLists=[]
    IDList=[]
    filePath = iB.fileLoc
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
    idHeader=iB.idHeaderName
    lngHeader = iB.lngHeaderName
    latHeader = iB.latHeaderName
    heightHeader = iB.heightHeaderName
    timeHeader = iB.timestampHeaderName
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
    #store Information in infobuffer
    iB.individuals=IDList
    iB.timeLists=timeLists
    iB.heightLists=heightLists
    iB.latLists=latLists
    iB.lngLists=lngLists
    