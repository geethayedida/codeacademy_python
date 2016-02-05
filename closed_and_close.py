# -*- coding: utf-8 -*-
"""
Created on Thu Feb 04 13:59:13 2016

@author: Geetha Yedida
"""

with open("text.txt", "w") as txtfile:
    txtfile.write("Goodbye to the course")
if txtfile.closed == False:
    txtfile.close()
print txtfile.closed