# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 11:46:15 2016

@author: Geetha Yedida
"""

def remove_duplicates(dup):
    out = []
    for i in dup:
        if i not in out:
           out.append(i)
    return out