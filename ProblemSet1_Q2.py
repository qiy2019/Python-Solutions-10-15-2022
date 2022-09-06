# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 16:25:42 2022

@author: qiy20
"""

count = 0;
i = 0;
s = 'azcbobobegghakl'
while i < len(s)-2:
    print(s[i+1:][0])
    if (s[i] == 'b' and s[i+1:][0] == 'o' and s[i+2:][0] == 'b'):
        count+=1
    i+=1
print("Number of time bob occurs is: " + str(count))