# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 11:45:22 2016

@author: Geetha Yedida
"""

def censor(text,word):
    if word in text:
        le = len(word)
        h =text.replace(word,'*'* le)
        return h