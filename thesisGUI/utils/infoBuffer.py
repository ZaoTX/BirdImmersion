# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 19:41:46 2020

@author: heziy
"""

class infoBuffer:
      def __init__(self):
            self.missingvalue=0
            self.startTime=''
            self.endTime=''
            self.startPos=''
            self.endPos=''
            self.numOfDatapoints=0
      def setMissing(self,num):
            self.missingvalue=num
      def setStartTime(self,startTime):
            self.startTime=startTime
      def setEndTime(self,endTime):
            self.endTime=endTime
      def setStartPos(self,pos):
            self.startPos=pos
      def setEndPos(self,pos):
            self.endPos=pos
      def setDataPoints(self,num):
            self.numOfDatapoints=num