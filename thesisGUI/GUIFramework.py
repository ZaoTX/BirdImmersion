# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 14:37:00 2020

@author: heziy
"""

import tkinter as tk
from tkinter import ttk


class MainGUI:
     root = tk.Tk()
     tabNotebook = ttk.Notebook(root)
     # Add different tabs
     tab1 = ttk.Frame(tabNotebook)
     tab2 = ttk.Frame(tabNotebook)
     tab3 = ttk.Frame(tabNotebook)
     tab4 = ttk.Frame(tabNotebook)
     tab5 = ttk.Frame(tabNotebook)
     tab6 = ttk.Frame(tabNotebook)
     tab7 = ttk.Frame(tabNotebook)
     
     def addTab(self):
           try:
                 from utils.Tabsetups import setupTab1,setupTab2,setupTab3,setupTab4,setupTab5
                 #set up style
                 self.setStyle()
                 
                 #setup tab1:
                 setupTab1(self.tab1)
                 #setup tab2:
                 
                 setupTab2(self.tab2)
                 
                 #setup tab3:
                 setupTab3(self.tab3)
                 #setup tab4:
                 setupTab4(self.tab4)
                 #setup tab5
                 setupTab5(self.tab5)
                 
                 self.tabNotebook.add(self.tab1, text = "Select Your Dataset")
                 self.tabNotebook.add(self.tab2, text = "Data filtering")
                 self.tabNotebook.add(self.tab3, text = "Split Dataset")
                 self.tabNotebook.add(self.tab4, text = "Clean Data")
                 self.tabNotebook.add(self.tab5, text = "Sample Dataset")
                 self.tabNotebook.add(self.tab6, text = "Aggregate/Summarize Data")
                 self.tabNotebook.add(self.tab7, text = "Report")
                 
                 self.tabNotebook.pack(fill ="both"
                                       ,expand=1
                                       ,padx=10, pady=10
                                       )
           except:
                 pass
               
     def setStyle(self):
           style= ttk.Style()
           style.theme_use('clam')
     
     def __init__(self):
           self.root.title("Movement Data Preprocessing")
           self.root.geometry("800x600")
           self.addTab()
           #self.root.mainloop()
#mainGui=MainGUI() 
         

           
          