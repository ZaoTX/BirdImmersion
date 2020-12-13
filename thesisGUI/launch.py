# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 14:28:46 2020

@author: heziy
"""

from GUIFramework import MainGUI
from utils.dataset import dataInfo
from utils.processingSetups  import processingSetups
from utils.infoBuffer import infoBuffer

pSetups=processingSetups()
d=dataInfo('','',[],[])
iB=infoBuffer()
main=MainGUI()
main.root.mainloop()

