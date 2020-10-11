# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 14:57:24 2020

@author: heziy
"""
import os
import csv
# this step use the filtered data and the output will be stored under the same directory
def individualSpliting(d,p):#d is dataset, p is processingsetups
      base_dir = d.workdir
      #specify the critical headers
      idHeader=p.idHeaderName
      filePath = base_dir+'/'+'filtered.csv'
      splitpath = base_dir+'/'+'SplitByID'
      if not os.path.exists(splitpath):
               os.makedirs(splitpath)
      csv_file=open(filePath, encoding='utf-8')
      csv_reader = csv.DictReader(csv_file, delimiter=',')
      fieldnames = p.choosenHeaders
      
      individual_id=[]
      for row in csv_reader:
        if individual_id==[]:
            last_id=None
        else:
            last_id=individual_id[-1]
        cur_id=row[idHeader]
        cur_id=cur_id.replace("/","-")#avoid bad id names
        individual_id.append(cur_id)
        if last_id!=cur_id:
            
            #csvfile_write.close()
            newpath = splitpath+'/'+cur_id
            #newpath = newpath.replace(" ","")
            if not os.path.exists(newpath):
                   os.makedirs(newpath)
            csvfile_write = open(newpath+'/'+cur_id+'.csv', 'a', newline='')
            writer = csv.DictWriter(csvfile_write
                                    ,fieldnames=fieldnames
                                    )
            writer.writeheader()
            
            writer.writerow(row)
        else:
            
            writer.writerow(row)
# d is launch.d, p is launch.pSetup, 
# reg is the Regular language of Time, aim is the split by which time skip
def splitingTime(d,p,reg,aim,sec):
      import re
      base_dir = d.workdir
      splitpath = base_dir+'/'+'SplitByTimeStamp'
      if not os.path.exists(splitpath):
             os.makedirs(splitpath)
      #specify the critical headers
#      idHeader=p.idHeaderName
#      latHeader=p.latHeaderName
#      lngHeader=p.lngHeaderName
#      heightHeader=p.heightHeaderName
      timestampHeader=p.timestampHeaderName
      filePath = base_dir+'/'+'filtered.csv'
      csv_file=open(filePath, encoding='utf-8')
      csv_reader = csv.DictReader(csv_file, delimiter=',')
      fieldnames = p.choosenHeaders
      
      
      if(aim=="1"):#Year
            lastYear=99999#initialize last time
            splitpath = splitpath+'/'+'ByYear'
            if not os.path.exists(splitpath):
                  os.makedirs(splitpath)
            for row in csv_reader:
                  cur_time=row[timestampHeader]
                  mat = re.match(reg,cur_time)
                  cur_Year=mat.group('YY')
                  if lastYear!=cur_Year:#not the same year
                        newpath = splitpath+'/'+cur_Year
                        if not os.path.exists(newpath):
                               os.makedirs(newpath)
                        csvfile_write = open(newpath+'/'+cur_Year+'.csv', 'a', newline='')# a for append (instead of overwrite)
                        writer = csv.DictWriter(csvfile_write,fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerow(row)
                              
                  else:
                              
                        writer.writerow(row)
                  lastYear=cur_Year
      elif(aim=="2"):#Month
            lastYear=99999#initialize last Year
            lastMonth=99999#initialize last Month
            splitpath = splitpath+'/'+'ByMonth'
            if not os.path.exists(splitpath):
                  os.makedirs(splitpath)
            for row in csv_reader:
                  
                  cur_time=row[timestampHeader]
                  
                  mat = re.match(reg,cur_time)
                  cur_Year=mat.group('YY')
                  cur_Month=mat.group('MM')
                  if (lastYear!=cur_Year and lastMonth!=cur_Month):#not the same Month
                        newpath = splitpath+'/'+cur_Year
                        #newpath = newpath.replace(" ","")
                        if not os.path.exists(newpath):
                               os.makedirs(newpath)
                        csvfile_write = open(newpath+'/'+cur_Month+'.csv', 'a', newline='')# a for append (instead of overwrite)
                        writer = csv.DictWriter(csvfile_write,fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerow(row)
                        
                  else:
                        
                        writer.writerow(row)
            lastYear=cur_Year
            lastMonth=cur_Month
      elif(aim=="3"): #Day
            lastYear=99999#initialize last Year
            lastMonth=99999#initialize last Month
            lastDay=99999#initialize last Day
            splitpath = splitpath+'/'+'ByDay'
            if not os.path.exists(splitpath):
                  os.makedirs(splitpath)
            for row in csv_reader:
                  
                  cur_time=row[timestampHeader]
                  
                  mat = re.match(reg,cur_time)
                  cur_Year=mat.group('YY')
                  cur_Month=mat.group('MM')
                  cur_Day=mat.group('DD')
                  if lastYear!=cur_Year and lastMonth!=cur_Month and lastDay!=cur_Day:#not the same Day
                        newpath = splitpath+'/'+cur_Year+'-'+cur_Month
                        #newpath = newpath.replace(" ","")
                        if not os.path.exists(newpath):
                               os.makedirs(newpath)
                        csvfile_write = open(newpath+'/'+cur_Day+'.csv', 'a', newline='')# a for append (instead of overwrite)
                        writer = csv.DictWriter(csvfile_write,fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerow(row)
                        
                  else:
                        
                        writer.writerow(row)
            lastYear=cur_Year
            lastMonth=cur_Month
            lastDay=cur_Day
       # The goal here is changed, 
       # we check if the time diff is less than the aim's setup 
       # and give the user the high temporal resolution period 
      elif(aim=="4"): #Hour
            from datetime import datetime
            threshold=3600#the threshold in second
            lastTime=''
            count=1
            splitpath = splitpath+'/'+'HighResolution_hour'
            if not os.path.exists(splitpath):
                  os.makedirs(splitpath)
            for row in csv_reader:
                  
                  cur_time=row[timestampHeader]
                  if (lastTime=='') :
                        csvfile_write = open(splitpath+'/'+str(count)+'.csv', 'a', newline='')
                        writer = csv.DictWriter(csvfile_write,fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerow(row)
                  else:
                        lastTimeObj=datetime.strptime(lastTime,'%Y-%m-%d %H:%M:%S.%f')
                        cur_timeObj=datetime.strptime(cur_time,'%Y-%m-%d %H:%M:%S.%f')
                        TimeDiff=abs((cur_timeObj-lastTimeObj).total_seconds())
                        if(TimeDiff<=threshold):
                              writer.writerow(row)
                        else:
                              count=count+1
                              csvfile_write = open(splitpath+'/'+str(count)+'.csv', 'a', newline='')
                              writer = csv.DictWriter(csvfile_write,fieldnames=fieldnames)
                              writer.writeheader()
                              writer.writerow(row)
                  lastTime=cur_time
            print("finished")
                              
      elif(aim=="5"):#Minute
            from datetime import datetime
            threshold=60#the threshold in second
            lastTime=''
            count=1
            splitpath = splitpath+'/'+'HighResolution_minute'
            if not os.path.exists(splitpath):
                  os.makedirs(splitpath)
            for row in csv_reader:
                  
                  cur_time=row[timestampHeader]
                  if (lastTime=='') :
                        csvfile_write = open(splitpath+'/'+str(count)+'.csv', 'a', newline='')
                        writer = csv.DictWriter(csvfile_write,fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerow(row)
                  else:
                        lastTimeObj=datetime.strptime(lastTime,'%Y-%m-%d %H:%M:%S.%f')
                        cur_timeObj=datetime.strptime(cur_time,'%Y-%m-%d %H:%M:%S.%f')
                        TimeDiff=abs((cur_timeObj-lastTimeObj).total_seconds())
                        if(TimeDiff<=threshold):
                              writer.writerow(row)
                        else:
                              count=count+1
                              csvfile_write = open(splitpath+'/'+str(count)+'.csv', 'a', newline='')
                              writer = csv.DictWriter(csvfile_write,fieldnames=fieldnames)
                              writer.writeheader()
                              writer.writerow(row)
                  lastTime=cur_time
            print("finished")
      elif(aim=="6"): #Second
            from datetime import datetime
            threshold=int(sec)#the threshold in second
            lastTime=''
            count=1
            splitpath = splitpath+'/'+'HighResolution_second'
            if not os.path.exists(splitpath):
                  os.makedirs(splitpath)
            for row in csv_reader:
                  
                  cur_time=row[timestampHeader]
                  if (lastTime=='') :
                        csvfile_write = open(splitpath+'/'+str(count)+'.csv', 'a', newline='')
                        writer = csv.DictWriter(csvfile_write,fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerow(row)
                  else:
                        lastTimeObj=datetime.strptime(lastTime,'%Y-%m-%d %H:%M:%S.%f')
                        cur_timeObj=datetime.strptime(cur_time,'%Y-%m-%d %H:%M:%S.%f')
                        TimeDiff=abs((cur_timeObj-lastTimeObj).total_seconds())
                        if(TimeDiff<=threshold):
                              writer.writerow(row)
                        else:
                              count=count+1
                              csvfile_write = open(splitpath+'/'+str(count)+'.csv', 'a', newline='')
                              writer = csv.DictWriter(csvfile_write,fieldnames=fieldnames)
                              writer.writeheader()
                              writer.writerow(row)
                  lastTime=cur_time
            print("finished")
      
      return