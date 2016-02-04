# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 15:20:54 2016

@author: Geetha Yedida
"""
input = 8


def check_bit4(inp):
    fourth = 0b1000
    desired = inp & fourth
    if desired >0:
        return "on"
    else:
        return "off"

print check_bit4(8)