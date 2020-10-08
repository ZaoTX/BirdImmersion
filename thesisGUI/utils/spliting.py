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
            newpath = base_dir+'/'+cur_id 
            #newpath = newpath.replace(" ","")
            if not os.path.exists(newpath):
                   os.makedirs(newpath)
            csvfile_write = open(newpath+'/'+cur_id+'.csv', 'w', newline='')
            writer = csv.DictWriter(csvfile_write,fieldnames=fieldnames)
            writer.writeheader()
        else:
            
            cur_time=row[timestampHeader]
            cur_lng=row[lngHeader]
            cur_lat=row[latHeader]
            cur_height=row[heightHeader]
            row_dict={idHeader:cur_id,
                      timestampHeader:cur_time,
                      lngHeader:cur_lng,
                      latHeader:cur_lat,
                      heightHeader:cur_height
                    }
            writer.writerow(row_dict)