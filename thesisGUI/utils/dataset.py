# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 16:47:39 2020

@author: heziy
"""
import csv

class initialData:
#      workdir=''
#      filepath=''
#      csv_file=csv.DictReader()
      def __init__(self,workdir,filepath,headers,individuals):
            self.workdir=workdir
            self.filepath=filepath
            self.csv_file=csv.DictReader(self.filepath)
            self.headers=headers
            self.individuals=individuals