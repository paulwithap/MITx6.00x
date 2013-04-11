class tPlot(object):

    def __init__(self, wordList):
        """
        wordList: A string containing the full path to a .txt file
        containing words separated by spaces.

        """

        self.wordList = open(wordList)

    def generateDicts(self, wordList):
        """

        takes in a wordList and generates two dictionaries used by
        the generatePlot() function

        """

        withT = {}
        totalWords = {}

        for line in wordList:
            words = line.split(' ')
            wordLength = 0
            for word in words:
                if len(word) > wordLength:  # check to see if the key exists
                    wordLength = len(word)
                    withT[wordLength] = 0
                    totalWords[wordLength] = 0
                if 't' in word:
                    withT[wordLength] += 1
                totalWords[wordLength] += 1

        print withT, totalWords

        return withT, totalWords

    def generatePlot(self):
        """
        Takes in 2 dictionaries:

        The first contains keys representing different word lengths and
        values representing the frequency of words at this length containing
        the letter 't'.

        The second contains keys representing word lengths and values
        representing the total number of words at this length.

        Returns a line graph with the probability a word will contain 't' for
        a given length.
        """
        import pylab

        # creates a list of the perecentages of 't' words per total words for each word length
        withT, totalWords = self.generateDicts(self.wordList)

        unroundedProbs = map(lambda x, y: float(x)/float(y), withT.values(), totalWords.values())
        roundedProbs = [round(x, 2) for x in unroundedProbs]

        pylab.figure(0)
        pylab.plot(totalWords.keys(), roundedProbs)
        pylab.xlabel("Word Length")
        pylab.ylabel("Probability Word Contains 't'")
        pylab.title("Probability a Word Contains 't' Vs. Word Length")
        pylab.show()
