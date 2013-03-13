def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    # Your code here
    if aStr == "":
        return 0
    else:
        count = 1
        return count + lenRecur(aStr[1:])
