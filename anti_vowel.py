# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 11:44:52 2016

@author: Geetha Yedida
"""

def anti_vowel(text):
    max = len(text)
    x = ''
    for i in range(0,max):
        if text[i] == 'a' or text[i] == 'A' or text[i] == 'E' or text[i] == 'I' or text[i] == 'O' or text[i] == 'U' or text[i] == 'e' or text[i] =='i' or text[i]=='o' or text[i]=='u' :
             x = x +''
        else:
            x = x + text[i]
    return x