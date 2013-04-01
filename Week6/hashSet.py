class hashSet(object):

    def __init__(self, numBuckets):
        '''

        numbuckets: int. The number of buckets this hash set will have.
        Raises ValueError if this value is not an integer, or if it is not 
        greater than zero.

        Sets up an empty hash set with numBuckets number of buckets.
        '''

        try:
            assert isinstance(numBuckets, int) and numBuckets > 0
        except AssertionError:
            raise ValueError, "numBuckets must be an integer greater than 0."
        else:
            self.hash = {x: [] for x in range(numBuckets)}

    def hashValue(self, e):
        '''

        e: an integer

        returns: a hash value for e, which is simply e modulo the number of 
        buckets in this hash
        set. Raises ValueError if e is not an integer.
        '''

        try:
            assert isinstance(e, int)
        except AssertionError:
            raise ValueError, "e must be an integer"
        else:
            return e % self.getNumBuckets()

    def member(self, e):
        '''

        e: an integer
        Returns True if e is in self, and False otherwise. Raises ValueError 
        if e is not an integer.
        '''
        try:
            assert isinstance(e, int)
        except AssertionError:
            raise ValueError, "e must be an integer"
        else:
            hashBucket = self.hashValue(e)
            return e in self.hash[hashBucket]

    def insert(self, e):
        '''

        e: an integer
        Inserts e into the appropriate hash bucket. Raises ValueError if e is 
        not an integer.
        '''
        try:
            assert isinstance(e, int)
        except AssertionError:
            raise ValueError, "e must be an integer"
        else:
            if not self.member(e):
                hashBucket = self.hashValue(e)
                self.hash[hashBucket].append(e)

    def remove(self, e):
        '''

        e: is an integer
        Removes e from self
        Raises ValueError if e is not in self or if e is not an integer.
        '''
        try:
            assert isinstance(e, int) and self.member(e)
        except AssertionError:
            raise ValueError, "e must be an integer in the hash"
        else:
            hashBucket = self.hashValue(e)
            self.hash[hashBucket].remove(e)

    def getNumBuckets(self):
        '''

        Returns the number of buckets in the hash.
        '''
        return len(self.hash.keys())
    def __str__(self):
        string = ""

        for key in self.hash:
            string += str(key) + ': ' + str(self.hash[key]) + "\n"

        return string
