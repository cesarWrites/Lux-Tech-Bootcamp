# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 22:35:41 2022

@author: Sarah
"""

#Program to find out if a year is a leap year or not
#accept year as input from user
year = int(input("Enter year: "))

#Divide century year by 100 to find out if its a leap year
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))
#Divide year by 4 to find out if its a leap year
elif (year % 4 == 0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))