# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 14:37:00 2020

@author: heziy
"""

import tkinter as tk
from tkinter import ttk
import tkinter.filedialog  as fd
from utils.loadData import setupData,setupWorkdir




#setup tab1: 
#   tab1 includes: select directory, select csv file' button , 
#   their label to explain the function

def setupTab1(tab):
     
     ########### Select directory path ###################
     # Label for information
     tab1_TextLabel = ttk.Label(tab, text= "Please select a directory for preprocessing, the output will be saved in this directory")
     tab1_TextLabel.place(relx = 0.1, rely = 0.1)
     
     # Button select dataset
     btn1 = ttk.Button(tab, text ='Select directory', command = lambda:open_dir()) 
     btn1.place(relx = 0.7, rely = 0.2)
     # Show the directory path
     strPath = tk.StringVar()
     ttk.Entry(tab,textvariable = strPath,
           width=65).place(
           relx=0.1,rely=0.2,
           height=30
           )
     import launch
     def open_dir():
         try:
           
           strPath.set('')
           filePath = fd.askdirectory()  
           if(filePath != ''):
                strPath.set(filePath)
                
                
                
                setupWorkdir(filePath,launch.d)
         except:pass
     ########### Select csv ###################
     tab1_TextLabel2 = ttk.Label(tab, text= "Please select your dataset(csv)")
     tab1_TextLabel2.place(relx = 0.1, rely = 0.3)
     btn2 = ttk.Button(tab, text ='Select file', command = lambda:open_dataset()) 
     btn2.place(relx = 0.7, rely = 0.4)
     
     #select a file
     strFname = tk.StringVar()
     ttk.Entry(tab,textvariable = strFname,
                 width=65).place(
                 relx=0.1,rely=0.4,
                 height=30
                 )
     def open_dataset():
           
           
           filename =  fd.askopenfilename(title="Select your dataset") 
           if(filename != ''):
                
                strFname.set(filename)
                
                
                try:
                      #setup csv.DictReader, filepath, workdir 
                      setupData(filename,launch.d)
                      choices=launch.d.headers
                      multibox.config(values=choices)
                      
                except: print('there is something wrong')
                updateTab2(launch.main.tab2,launch.d,launch.main)

      ############ short summary#############
     tab1_TextLabel3 = ttk.Label(tab, text= "The headers of the csv file are: ")
     tab1_TextLabel3.place(relx = 0.1, rely = 0.5) 
     choices=[]
     multibox=ttk.Combobox(tab,values=choices
                           ,width=40
                           ,font=12
                           )
     
     multibox.place(relx = 0.4, rely = 0.5)   
#setup tab2: 
#   tab2 includes: mutiple selection of headers we want to keep, launch button , 
#   their label to explain the function
#    

def setupTab2(tab):
      
      
      
      tab2_TextLabel1 = ttk.Label(tab, text= "Please choose the headers you want to keep")
      tab2_TextLabel1.place(relx = 0.1, rely = 0.1)
      
      
def updateTab2(tab,d,mainGui):
      #clean tab
      for child in tab.winfo_children():
           child.destroy()
      s = ttk.Style()
      bg = s.lookup('TFrame', 'background')
      
      listbox = tk.Listbox(tab, selectmode = "multiple"  
               ) 
      scrollbar = tk.Scrollbar(listbox,orient=tk.VERTICAL)
      scrollbar.pack( side = tk.RIGHT, fill = 'y')
      listbox.config(yscrollcommand = scrollbar.set)
      listbox.place(relx = 0.1, rely = 0.2,
                    height = 400,width=500) 
     
      
      tab2_TextLabel1 = ttk.Label(tab, text= "Please choose the headers you want to keep")
      tab2_TextLabel1.place(relx = 0.1, rely = 0.1)
      headerList = d.headers
      count=1
      for i in headerList:
            #print(i)
             listbox.insert(tk.END, i) 
             listbox.config( bg = bg) 
             count=count+1
       #setup checkbox for default setting
      var1=tk.BooleanVar()
      useDefault=ttk.Checkbutton(tab, text="Use Default", variable=var1)
      useDefault.place(relx = 0.8, rely = 0.8)
      #confirm button
      btn1 = ttk.Button(tab, text ='Confirm', command = lambda:confirm()) 
      btn1.place(relx = 0.8, rely = 0.9)
      import launch
      def confirm():
            values = [str(listbox.get(idx)) for idx in listbox.curselection()]
            #get the header according to the user's choose
            if(var1.get()):
                  #the user use the default headers and the headers they selected
                  launch.processingSetups.useDefaultInfo(launch.processingSetups)
                  launch.processingSetups.choosedHeaders=launch.processingSetups.choosedHeaders+values
                  #make value unique
                  launch.processingSetups.choosedHeaders=list(set(launch.processingSetups.choosedHeaders))
                  
            
            else:
                  #the user only use the headers they selected
                  launch.processingSetups.choosedHeaders=values
                  #print (', '.join(launch.processingSetups.choosedHeaders))
            from utils.datafiltering import filtering
            filtering(launch.processingSetups.choosedHeaders,launch.d)
                  
#setup tab3: 
#   tab3 includes: selection of mehtods, launch button , 
#   their label to explain the function
# 

def setupTab3(tab):
     # Label for information
     tab3_TextLabel1 = ttk.Label(tab, text= "How to deal with missing value")
     tab3_TextLabel1.place(relx = 0.1, rely = 0.2)
     
     choices=["remove the data with missing value","linear interpolation"]
     multibox=ttk.Combobox(tab,values=choices
                           ,width=40
                           ,font=12
                           )
     multibox.place(relx = 0.2, rely = 0.3)
     
     launchBtn= ttk.Button(tab, text="launch", command = lambda: cleandataset())
     launchBtn.place(relx = 0.8, rely = 0.3)
     # Label for information
     tab3_TextLabel2 = ttk.Label(tab, text= "How long in second do you want for a timeskip(set up for linear interpolation)")
     tab3_TextLabel2.place(relx = 0.1, rely = 0.4)
     #
     Entry=ttk.Entry(tab
                     ,width=5
                           )
     Entry.place(relx = 0.8, rely = 0.4)
     # Label for information
     tab3_TextLabel3 = ttk.Label(tab, text= "Here should be some comments about advantages and disadvantages for each method")
     tab3_TextLabel3.place(relx = 0.1, rely = 0.5)
     
     
     def cleandataset():
#           choice = multibox.get()
#           print(choice)
#           ind=choices.index(choice,0,len(choices))
#           print(ind)
#           if(ind==0):#remove value
#                 return
#           elif(ind==1):#linear interpolation
#                 return
#           else:#remove value
#             return
           return

def setupTab4(tab):
     # Label for information
     tab4_TextLabel1 = ttk.Label(tab, text= "You can decide split by year, month,day,seconds etc.")
     tab4_TextLabel1.place(relx = 0.2, rely = 0.2)
     # entry for year
     Entry2=ttk.Entry(tab
                     ,width=5
                           )
     Entry2.place(relx = 0.2, rely = 0.3)
     
     tab4_TextLabel2 = ttk.Label(tab, text= "Year")
     tab4_TextLabel2.place(relx = 0.25, rely = 0.3)
     # entry for month
     Entry3=ttk.Entry(tab
                     ,width=5
                           )
     Entry3.place(relx = 0.3, rely = 0.3)
     
     tab4_TextLabel3 = ttk.Label(tab, text= "Month")
     tab4_TextLabel3.place(relx = 0.35, rely = 0.3)
     #  entry for day
     Entry4=ttk.Entry(tab
                     ,width=5
                           )
     Entry4.place(relx = 0.42, rely = 0.3)
     
     tab4_TextLabel4 = ttk.Label(tab, text= "Day")
     tab4_TextLabel4.place(relx = 0.47, rely = 0.3)
     #  entry for min
     Entry5=ttk.Entry(tab
                     ,width=5
                           )
     Entry5.place(relx = 0.52, rely = 0.3)
     
     tab4_TextLabel1 = ttk.Label(tab, text= "Minute")
     tab4_TextLabel1.place(relx = 0.57, rely = 0.3)
     # entry for seconds
     Entry6=ttk.Entry(tab
                     ,width=5
                           )
     Entry6.place(relx = 0.64, rely = 0.3)
     tab4_TextLabel1 = ttk.Label(tab, text= "Second")
     tab4_TextLabel1.place(relx = 0.69, rely = 0.3)
     
     # Label for information
     tab4_TextLabel1 = ttk.Label(tab, text= "You can decide split by which individual")
     tab4_TextLabel1.place(relx = 0.2, rely = 0.4)
     choices=["All"]
     multibox=ttk.Combobox(tab,values=choices
                           ,width=40
                           ,font=12
                           )
     multibox.place(relx = 0.2, rely = 0.5)