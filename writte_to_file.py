# -*- coding: utf-8 -*-
"""
Created on Thu Feb 04 13:29:25 2016

@author: Geetha Yedida
"""

my_list = [i**2 for i in range(1,11)]

my_file = open("output.txt", "r+")

# Add your code below!
for i in my_list:
    my_file.write(str(i))
    my_file.write("\n")
my_file.close()