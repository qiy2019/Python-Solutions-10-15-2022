def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if (exp == 0 and base > 0): return 1.0000
    count = base;
    for i in range(1, exp):
        count *= base
    return count