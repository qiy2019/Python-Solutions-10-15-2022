def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    if (len(aDict.values()) == 0): return None
    max = -1;
    keys = aDict.keys()
    for k in keys:
        if (len(aDict[k]) > max): 
            letter = k
            max = len(aDict[k])
    return letter