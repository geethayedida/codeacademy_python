# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 13:33:02 2016

@author: Geetha Yedida
"""

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message= filter(lambda x: x != 'X' ,garbled)
print message