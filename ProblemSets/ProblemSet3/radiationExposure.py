def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    # FILL IN YOUR CODE HERE...

    import numpy as np

    radiation = 0.0

    for i in np.arange(start, stop, step):
        if stop == 0:
            return 0
        if stop == 1:
            return f(i)*step
        else:
            radiation += f(i)*step
    return radiation
