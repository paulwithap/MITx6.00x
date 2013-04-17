import intDictTests

def mostInsertions(low, high, buckets):
    """
    low: an integer, the number of insertions where calculated
    collision probability is known to be < 0.99

    high: an integer, the number of insertions where calculated
    collision probability is known to be > 0.99

    buckets: an integer, the number of buckets

    Uses a collision probability function to determine the largest
    number of possible insertions with a calculated collision
    probability of < 0.99 for a given number of buckets.
    """
    PROB = 0.99
    middle = (low + high)/2

    if intDictTests.collision_prob(buckets, middle) < PROB and high - middle == 1:
        return middle
    elif intDictTests.collision_prob(buckets, middle) < PROB:
        return mostInsertions(middle, high, buckets)
    else:
        return mostInsertions(low, middle, buckets)
