# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 16:55:04 2022

@author: qiy20
"""

# iterative
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if (a == b): return a
    result = 0
    bigger = max(a, b)
    for i in range(1, bigger):
        if (a%i == 0 and b%i == 0):
            result = max(result, i)
    return result

# recursive
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if (b == 0): return a
    else: return gcdRecur(b, a%b)