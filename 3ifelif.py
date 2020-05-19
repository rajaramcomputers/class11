# -*- coding: utf-8 -*-
"""
Created on Tue May 19 13:10:13 2020

@author: VARDHINI
"""

line = input("Enter the Line: ")

string = input ("Enter the String: ")

if string in line:
    print(string, ' is part of ', line)
else:
    print(string, ' is not part of ', line)