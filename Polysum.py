# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 10:49:44 2022

@author: qiy20
"""

def polysum(n, s):
    """
    import math and return area + perimeter rounded to 4 decimal places

    Parameters
    ----------
    n: number of sides
    s: length of sides

    Returns
    -------
    float

    """
    
    import math
    
    area = (0.25 * n * (s ** 2)) / math.tan(math.pi / n)
    perimeter = (s * n) ** 2
    return round(area + perimeter, 4)
