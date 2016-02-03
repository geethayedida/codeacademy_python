# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 11:15:37 2016

@author: Geetha Yedida
"""

from datetime import datetime
now = datetime.now()

print '%s/%s/%s %s:%s:%s' % ( now.month, now.day,now.year,now.hour, now.minute,now.second)