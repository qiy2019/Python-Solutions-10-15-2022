# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 10:56:23 2022

@author: qiy20
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    result = ()
    for i in range(0, len(aTup), 2):
        result += (aTup[i], )
    return result
print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))