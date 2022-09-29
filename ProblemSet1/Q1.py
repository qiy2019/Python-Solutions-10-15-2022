# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 16:24:43 2022

@author: qiy20
"""

count = 0;
s = 'azcbobobegghakl'
for c in s:
    if (c == 'a' or c == 'e' or 
    c == 'i' or c == 'o' or c == 'u'):
        count+=1
        
print("Number of vowels: " + str(count))
