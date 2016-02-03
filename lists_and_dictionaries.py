# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 11:26:41 2016

@author: Geetha Yedida
"""

shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0
    for i in food:
        if stock[str(i)] > 0:
            total = prices[str(i)] + total
            stock[str(i)]= stock[str(i)] -1
        
    return total

compute_bill(['apple'])