# -*- coding: utf-8 -*-
"""
Created on Tue May 19 12:14:34 2020

@author: VARDHINI
"""

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
op = str.strip(input("Enter the operator [+ , - , * ,/] : "))
result = 0.0

if op == '+':
    result = num1 + num2
    
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
elif op == '/':
    result = num1 / num2
else:
    print ("Invalid Operator")

print("Operator used is", op, "first number is", num1, "second number is", num2, "result is", result)

