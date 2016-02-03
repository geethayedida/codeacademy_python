# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 11:39:22 2016

@author: Geetha Yedida
"""

fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    if f == 'Hi':
        print 'A tomato is not a fruit!' # (It actually is.)
        break
    print 'A', f
else:
    print 'A fine selection of fruits!'