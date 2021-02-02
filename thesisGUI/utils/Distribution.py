# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 22:36:36 2021

@author: ZiyaoHe
"""
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatch
'''
 A Horizontal Distribution of the individual using matplotlib
'''
def plotHorizontal(main,iB,d):
    # find individual list
    IDList=d.individuals
    # timeLists=d.TimeLists
    #heightLists=d.heightLists
    latLists=d.latLists
    lngLists=d.lngLists
    
    # number of individuals
    num=len(IDList)
    
    maxLats=[]
    minLats=[]
    maxLngs=[]
    minLngs=[]
    # for each individual
    # we find a pair of min max value for each individual's lat lng
    for i in range(0,num):
        latList= latLists[i]
        latList = [float(i) for i in latList]
        lngList=lngLists[i]
        lngList = [float(i) for i in lngList]
        maxLat=max(latList)
        minLat=min(latList)
        maxLng=max(lngList)
        minLng=min(lngList)
        maxLats.append(maxLat)
        minLats.append(minLat)
        maxLngs.append(maxLng)
        minLngs.append(minLng)
    #find the largest lat,lng and the smallest lat lng as range of axis
    theMinLat=min(minLats)
    
    theMaxLat=max(maxLats)
    
    
    theMinLng=min(minLngs)
    
    theMaxLng=max(maxLngs)
    xlim_min= theMinLng-(theMaxLng-theMinLng)*0.3
    if(xlim_min<-180):
        xlim_min=-180
        
    xlim_max= theMaxLng+(theMaxLng-theMinLng)*0.3
    if(xlim_max>180):
        xlim_max=180
        
    ylim_min= theMinLat-(theMaxLat-theMinLat)*0.3
    if(ylim_min<-90):
        ylim_min=-90
        
    ylim_max= theMaxLat+(theMaxLat-theMinLat)*0.3
    if(ylim_max>90):
        ylim_max=90
    main.axis(xmin=xlim_min,xmax=xlim_max, ymin=ylim_min, ymax=ylim_max)
    #main.ylim([theMinLat,theMaxLat])
    #generate a colormap that gives distinct color from 0 to num
    colormap=plt.cm.get_cmap('hsv', num)
    # define the rectangle
    for i in range(0,num):
        minLati=minLats[i]
        maxLati=maxLats[i]
        minLngi=minLngs[i]
        maxLngi=maxLngs[i]
        #add id name:
        idName=IDList[i]
        width=maxLngi-minLngi
        height=maxLati-minLati
        color = colormap(i)
        #colors.append(color)
        rect = mpatch.Rectangle((minLngi,minLati),width , height, linewidth=1,edgecolor=color, alpha = 0.3, facecolor=color,label=idName)
        main.add_patch(rect)
    main.legend(loc='best')
#    cdict=dict(zip(IDList,colors))
#    for n in IDList:
        
        

#        midLat=(maxLati+minLati)/2
#        midLng=(maxLngi+minLngi)/2
        #main.text(midLng,midLat,idName)
'''
 Assumption: for each individual it starts from first timestamp and end at the last timestamp 
'''
def plotTimeline(fig,main,iB,d):
    import matplotlib.dates as md
    import pandas as pd
    # See https://github.com/facebook/prophet/issues/999
    #register_matplotlib_converters()
    #warnings.warn(msg, FutureWarning)
    pd.plotting.register_matplotlib_converters()
    # find individual list
    IDList=d.individuals
    timeLists=d.TimeLists
    # number of individuals
    num=len(IDList)
    
    minTimestamps=[]
    maxTimestamps=[]
    # for each individual
    # we find a pair of min max value for timestamp
    for i in range(0,num):
        timeList=timeLists[i]
        timeList=pd.to_datetime(timeList)
        idName=IDList[i]
        minTimestamps.append(timeList[0])
        maxTimestamps.append(timeList[-1])
        main.scatter(timeList, [i]*len(timeList),
           marker='s', label=idName)
    maxTimestamp=max(maxTimestamps)
    minTimestamp=min(minTimestamps)
    diff = maxTimestamp-minTimestamp
    xlim_max=maxTimestamp+0.1*diff
    xlim_min=minTimestamp-0.1*diff
    main.axis(xmin=xlim_min,xmax=xlim_max)
    #main.get_xaxis().set_major_locator()
    xfmt = md.DateFormatter('%Y-%m-%d %H:%M:%S')
    main.xaxis.set_major_formatter(xfmt)
    fig.autofmt_xdate()
    if(7>float(diff.days)>1):
        main.get_xaxis().set_major_locator(md.DayLocator(interval=1))
    elif(30>float(diff.days)>=7):
        main.get_xaxis().set_major_locator(md.WeekdayLocator(interval=1))
    elif(float(diff.days)>=30):
        main.get_xaxis().set_major_locator(md.MonthLocator(interval=1))
    else:
        main.get_xaxis().set_major_locator(md.HourLocator(interval=1))
    main.legend(loc='best')
