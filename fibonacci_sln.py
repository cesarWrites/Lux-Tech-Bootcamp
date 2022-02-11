# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 23:29:13 2022

@author: Dell
"""


n = int(input("Enter the number to test: "))
c=0
a=1
b=1
if n==0 or n==1:
    print("Number is fibonacci ")
else:
    while c<n:
        c=a+b
        b=a
        a=c
    if c==n:
        print("Number is fibonacci ")
    else:
        print("Number is not fibonacci ")