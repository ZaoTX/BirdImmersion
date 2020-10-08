# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 20:08:54 2020

@author: heziy
"""

class processingSetups:
      def __init__(self):
            self.choosenHeaders=[]
            self.idHeaderName=''
            self.latHeaderName=''
            self.lngHeaderName=''
            self.heightHeaderName=''
            self.timestampHeaderName=''
      def useDefaultInfo(self):
            self.choosenHeaders=['individual-local-identifier','location-lat','location-long','height-above-ellipsoid','timestamp']
            self.idHeaderName= 'individual-local-identifier'
            self.latHeaderName='location-lat'
            self.lngHeaderName='location-long'
            self.heightHeaderName='height-above-ellipsoid'
            self.timestampHeaderName='timestamp'
      def setBasicInfo(self,idHeaderName,latHeaderName,lngHeaderName,heightHeaderName,timestampHeaderName):
            self.choosenHeaders=[idHeaderName,latHeaderName,lngHeaderName,heightHeaderName,timestampHeaderName]
            self.idHeaderName= idHeaderName
            self.latHeaderName=latHeaderName
            self.lngHeaderName=lngHeaderName
            self.heightHeaderName=heightHeaderName
            self.timestampHeaderName=timestampHeaderName