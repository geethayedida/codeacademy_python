# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 11:18:39 2016

@author: Geetha Yedida
"""

print 'Welcome to the Pig Latin Translator!'

# Start coding here!
original = raw_input("Enter a word:")
if len(original) > 0 and original.isalpha():
    print original
else:
    print "empty"