# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 14:28:46 2020

@author: heziy
"""

from GUIFramework import MainGUI
from utils.dataset import initialData
from utils.processingSetups  import processingSetups



pSetups=processingSetups()
d=initialData('','',[],[])
main=MainGUI()
main.root.mainloop()