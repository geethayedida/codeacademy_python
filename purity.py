# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 11:45:49 2016

@author: Geetha Yedida
"""

def purify(num):
    out = []
    for i in range(len(num)):
        if num[i]%2 ==0:
            out.append(num[i])
    else:
        return out