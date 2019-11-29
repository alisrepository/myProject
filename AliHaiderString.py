# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 20:49:29 2019

@author: ALI
"""
#ALI HAIDER; REG NO. PIAIC69857

# RETURNS TRUE IF ALL ARE DIGITS (NUMBERS) AND RETURNS FALSE IF EVEN SINGLE ENTRY IN STRING IS NOT DIGIT
def isDigit(num):
    isNum = False
    i = 0
    while(i < len(num)):
        if(ord(num[i]) > 47 and ord(num[i])<58):
            isNum = True
        else:
            return False
        i += 1
    return isNum
        
print("ENTER VALUE IS DIGIT " + str(isDigit(input("ENTER INPUT TO CHECK IF ITS DIGIT: "))))