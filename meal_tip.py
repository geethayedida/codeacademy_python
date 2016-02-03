# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 11:12:27 2016

@author: Geetha Yedida
"""

# Assign the variable total on line 8!

meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal * tax
total = meal + meal * tip

print("%.2f" % total)