# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 11:26:13 2016

@author: Geetha Yedida
"""

prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}
stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}

for key in prices:
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]

total = 0

for p in prices:
    total_val =  stock[p] * prices[p]
    total = total + total_val
print total