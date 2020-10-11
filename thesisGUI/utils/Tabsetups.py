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
      
      def confirm():
            import launch
            values = [str(listbox.get(idx)) for idx in listbox.curselection()]
            #get the header according to the user's choose
            if(var1.get()):
                  #the user use the default headers and the headers they selected
                  launch.pSetups.useDefaultInfo()
                  launch.pSetups.choosenHeaders=launch.pSetups.choosenHeaders+values
                  #make value unique
                  launch.pSetups.choosenHeaders=list(set(launch.pSetups.choosenHeaders))
                  
            
            else:
                  #the user only use the headers they selected
                  launch.processingSetups.choosenHeaders=values
            from utils.datafiltering import filtering
            filtering(launch.pSetups.choosenHeaders,launch.d)
                  
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
     tab4_TextLabel1 = ttk.Label(tab, text= "Here you can decide whether to split by individual's Id or year, month etc.")
     tab4_TextLabel1.place(relx = 0.1, rely = 0.1)
     v = tk.StringVar(tab,"1") 
     checkbox1=ttk.Radiobutton(tab, text="Split by timestamp", variable=v,value="1")
     checkbox1.place(relx = 0.1, rely = 0.2)
     checkbox2=ttk.Radiobutton(tab, text="Split by individual", variable=v,value="2")
     checkbox2.place(relx = 0.1, rely = 0.8)
     v2 = tk.StringVar(tab,"1")
     # entry for year
     checkbox3=ttk.Radiobutton(tab, text="Year", variable=v2,value="1")
     checkbox3.place(relx = 0.1, rely = 0.3)
     
     # entry for month
     checkbox4=ttk.Radiobutton(tab, text="Month", variable=v2,value="2")
     checkbox4.place(relx = 0.2, rely = 0.3)
     
     #  entry for day
     checkbox5=ttk.Radiobutton(tab, text="Day", variable=v2,value="3")
     checkbox5.place(relx = 0.3, rely = 0.3)
     
     #  entry for min
     checkbox6=ttk.Radiobutton(tab, text="Hour", variable=v2,value="4")
     checkbox6.place(relx = 0.4, rely = 0.3)
     #  entry for min
     checkbox7=ttk.Radiobutton(tab, text="Minute", variable=v2,value="5")
     checkbox7.place(relx = 0.5, rely = 0.3)
     # entry for seconds
     checkbox7=ttk.Radiobutton(tab, text="Second", variable=v2,value="6")
     checkbox7.place(relx = 0.6, rely = 0.3)
     
     # Label for information
     tab4_TextLabel3 = ttk.Label(tab, text= "If the regular language of timestamp doesn't match, you can write your own:(copy)")
     tab4_TextLabel3.place(relx = 0.1, rely = 0.4)
     
     # Label for information
     defaultReg=tk.StringVar()
     defaultReg.set(r"((?P<YY>\d{4})-(?P<MM>\d{1,2})-(?P<DD>\d{1,2}) (?P<h>\d{1,2}):(?P<min>\d{2}):(?P<sec>\d{2}[.]\d{3}))")
     entry1=tk.Entry(tab,
           width=108)
     entry1.config(textvariable = defaultReg,state='readonly',relief='flat')
     entry1.place(relx = 0.1, rely = 0.5)
     tab4_TextLabel5 = ttk.Label(tab, text= "Here you can write your regular language for timestamp")
     tab4_TextLabel5.place(relx = 0.1, rely = 0.6)
     textVar=tk.StringVar()
     entry2=tk.Entry(tab,
           width=108,
           textvariable = textVar,
           relief='flat')
     entry2.place(relx = 0.1, rely = 0.7)
     #defaultReg.set("((?P<DD>\d{1,2})/(?P<MM>\d{1,2})/(?P<YY>\d{4}) (?P<h>\d{1,2}):(?P<min>\d{2}):(?P<sec>\d{2}) (?P<TT>[AM|PM]{2}))")
     #confirm button
     btn1 = ttk.Button(tab, text ='Confirm', command = lambda:confirm()) 
     btn1.place(relx = 0.8, rely = 0.9)
     
     
     def confirm():
           #check spilt option
           if(v.get()=="1"):#split by timestamp
                 reg=''
                 if(entry2.get()!=''):
                       reg=entry2.get()
                 else:
                       reg=r"((?P<YY>\d{4})-(?P<MM>\d{1,2})-(?P<DD>\d{1,2}) (?P<h>\d{1,2}):(?P<min>\d{2}):(?P<sec>\d{2}[.]\d{3}))"
                 print(reg)
                 #split by which time difference
                 typ=v2.get()
                 import launch
                 from utils.spliting import splitingTime
                 splitingTime(launch.d,launch.pSetups,reg,typ)
                 return
#                 
           else:#split by inidividual
                 import launch
                 from utils.spliting import individualSpliting
                 individualSpliting(launch.d,launch.pSetups)
                 #return
           