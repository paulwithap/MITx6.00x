def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    count = 0
    for key in aDict.keys():
        if aDict[key] != []:
            for value in aDict[key]:
                count += 1
    return count
