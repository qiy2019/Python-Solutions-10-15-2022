def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    
    if (len(aStr) == 0): return False
    elif (aStr[0] == char): return True
    else: return isIn(char, aStr[1:])