def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    # import random (MIT's grader seems to have already done this)

    bucket = ['red', 'green'] * 3
    sameColor = 0.0

    for trial in range(numTrials):
        balls = random.sample(bucket, 3)
        if balls.count('red') == 3 or balls.count('green') == 3:
            sameColor += 1

    return sameColor/numTrials
