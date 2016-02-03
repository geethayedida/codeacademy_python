# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 11:41:35 2016

@author: Geetha Yedida
"""

def reverse(text):
      string = ""
      i = len(text)
      while i > 0:
            string = string + text[i-1]
            i -= 1
      return string