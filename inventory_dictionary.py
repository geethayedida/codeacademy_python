# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 11:24:23 2016

@author: Geetha Yedida
"""

inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf'],
    'pocket':['seashell', 'strange berry','lint']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 
inventory['backpack'].sort()
# Your code here
inventory['backpack'].remove('dagger')
inventory['gold'] = 550