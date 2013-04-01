def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    if len(aDict.values()) == 0:
        return None
    count = 0
    bigValue = []
    for value in aDict.values():
        if len(value) > count:
            count = len(value)
            bigValue = value
    for key in aDict:
        if bigValue == aDict[key]:
            return key
