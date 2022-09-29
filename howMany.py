def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    length = 0
    for i in aDict.values():
        length += len(i)
    return length