# -*- coding: utf-8 -*-
"""
Created on Tue May 19 11:17:38 2020

@author: VARDHINI
"""

radius = float(input("Enter radius of the circle: "))

print("1.Calculate Area:")
print("2.Calculate Perimeter")

choice = int(input("Enter the Choice 1 or 2: "))
if choice == 1:
    area = 3.14159 * radius * radius
    print("Area of Circle with radius ", 'is', area)
else:
    perm = 2*3.14159 * radius
    print("Perimeter of Circule with radius", radius , 'is', perm)
    5