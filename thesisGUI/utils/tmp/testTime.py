# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 11:58:07 2020

@author: heziy
"""
import re
from datetime import datetime
test_date='9/3/2020 2:00:45 PM'
regStr=r"((?P<DD>\d{1,2})/(?P<MM>\d{1,2})/(?P<YY>\d{4}) (?P<h>\d{1,2}):(?P<min>\d{2}):(?P<sec>\d{2}) (?P<TT>[AM|PM]{2}))"
mat = re.match(regStr,test_date)
print(mat.group('TT'))
print (type(mat.group(0)))