# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 08:33:28 2016

@author: hclqaVirtualBox1
"""

import datetime

# datetime() receives as parameter:
# year, month, day, hour, minute, second and
# returns an object of type datetime
dt = datetime.datetime(2020, 12, 31, 23, 59, 59)

# Objects date and time can be created from
# a datetime object
date = dt.date()
hour = dt.time()
# How many time to 12/31/2020
dd = dt - dt.today()

print ('Date:', date)
print ('Hour:', hour)
print ('How many time to 12/31/2020:', dd)
today = dt.today()
print(today)
