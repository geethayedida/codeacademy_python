# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 11:31:27 2016

@author: Geetha Yedida
"""

n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
    result = ""
    for word in words:
        result = result + word
    return result


print join_strings(n)