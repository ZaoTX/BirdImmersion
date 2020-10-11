# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 11:58:07 2020

@author: heziy
"""
import re
from datetime import datetime
test_date='2019-10-01 02:00:00.000'
regStr=r"((?P<YY>\d{4})-(?P<MM>\d{1,2})-(?P<DD>\d{1,2}) (?P<h>\d{1,2}):(?P<min>\d{2}):(?P<sec>\d{2}[.]\d{3}))"
mat = re.match(regStr,test_date)
print(mat.group('sec'))
print (type(mat.group(0)))
#import time
#print(time.strptime('30/03/09 16:31:32', '%d/%m/%y %H:%M:%S'))