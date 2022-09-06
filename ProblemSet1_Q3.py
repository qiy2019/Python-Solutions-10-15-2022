# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 16:27:33 2022

@author: qiy20
"""

str = ""
s = 'azcbobobegghakl'
strs = []
alphabet = "abcdefghijklmnopqrstuvwxyz"
i = 0;
while i < len(s):
    str = s[i]
    for j in s[i+1:]:
        if (alphabet.index(str[-1]) <= alphabet.index(j)):
            str += j
        else: break
    strs.append(str)
    str = "";
    i+=1
    
result = sorted(strs, key=len, reverse=True)[0]
print("Longest substring in alphabetical order is: " + result)