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
      latHeader=p.latHeaderName
      #print(latHeader)
      lngHeader=p.lngHeaderName
      heightHeader=p.heightHeaderName
      timestampHeader=p.timestampHeaderName
      filePath = base_dir+'/'+'filtered.csv'
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
            newpath = base_dir+'/'+cur_id 
            #newpath = newpath.replace(" ","")
            if not os.path.exists(newpath):
                   os.makedirs(newpath)
            csvfile_write = open(newpath+'/'+cur_id+'.csv', 'a', newline='')
            writer = csv.DictWriter(csvfile_write
                                    ,fieldnames=fieldnames
                                    )
            writer.writeheader()
            cur_time=row[timestampHeader]
            cur_lng=row[lngHeader]
            
#            if(row[lngHeader]==row['location-long']):
#                  print("equal")
#                  if(row[lngHeader]==''):
#                        print("empty")
#            else:print("not equal")
                  
            cur_lat=row[latHeader]
            cur_height=row[heightHeader]
            row_dict={idHeader:cur_id,
                      lngHeader:cur_lng,
                      latHeader:cur_lat,
                      heightHeader:cur_height,
                      timestampHeader:cur_time
                    }
            writer.writerow(row_dict)
        else:
            
            cur_time=row[timestampHeader]
            cur_lng=row[lngHeader]
            cur_lat=row[latHeader]
            cur_height=row[heightHeader]
            print(type(cur_lng))
            row_dict={idHeader:cur_id,
                      lngHeader:cur_lng,
                      latHeader:cur_lat,
                      heightHeader:cur_height,
                      timestampHeader:cur_time
                     }
            writer.writerow(row_dict)
# d is launch.d, p is launch.pSetup, 
# reg is the Regular language of Time, aim is the split by which time skip
#def splitingTime(d,p,reg,aim):
#      import re
#      base_dir = d.workdir
#      #specify the critical headers
#      idHeader=p.idHeaderName
#      latHeader=p.latHeaderName
#      lngHeader=p.lngHeaderName
#      heightHeader=p.heightHeaderName
#      timestampHeader=p.timestampHeaderName
#      filePath = base_dir+'/'+'filtered.csv'
#      csv_file=open(filePath, encoding='utf-8')
#      csv_reader = csv.DictReader(csv_file, delimiter=',')
#      fieldnames = p.choosenHeaders
#      lastTime=99999#initialize last time
#      timeskip=1#initialize time diff
#      if(v2.get()=="1"):#Year
#            count=0
#            for row in csv_reader:
#                  cur_time=row[timestampHeader]
#                  mat = re.match(reg,cur_time)
#                  cur_Year=mat.group('YY')
#                  if(lastTime==99999):
#                        lastTime=cur_time
#                  else:
#                        if lastTime!=cur_time:#not the same year
#                              newpath = base_dir+'/'+count 
#                              #newpath = newpath.replace(" ","")
#                              if not os.path.exists(newpath):
#                                     os.makedirs(newpath)
#                              csvfile_write = open(newpath+'/'+cur_id+'.csv', 'w', newline='')
#                              writer = csv.DictWriter(csvfile_write,fieldnames=fieldnames)
#                              writer.writeheader()
#                              count=count+1
#                        else:
#                              
#                              cur_time=row[timestampHeader]
#                              cur_lng=row[lngHeader]
#                              cur_lat=row[latHeader]
#                              cur_height=row[heightHeader]
#                              row_dict={idHeader:cur_id,
#                                        timestampHeader:cur_time,
#                                        lngHeader:cur_lng,
#                                        latHeader:cur_lat,
#                                        heightHeader:cur_height
#                                      }
#                              writer.writerow(row_dict)
#                        lastTime=cur_time
#           elif(v2.get()=="2"):#Month
#           elif(v2.get()=="3"): #Day
#           elif(v2.get()=="4"): #Hour
#           elif(v2.get()=="5"):#Minute
#           elif(v2.get()=="6"): #Second
#      
#      return