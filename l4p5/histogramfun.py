import pylab

# You may have to change this path
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    n = float(len(wordList))
    vowelProportions = [propVowels(word) for word in wordList]
    pylab.hist(vowelProportions, numBins)
    labelPlot()
    pylab.show()

def labelPlot():
    pylab.title("Proportion of vowels")
    pylab.ylabel("Number of words")
    pylab.xlabel("Proportion of vowels in each word")

def numVowels(word):
    cnt = 0
    vowels = ["a", "e", "i", "o", "u"]
    for c in word:
        if c in vowels:
            cnt += 1
    return cnt

def propVowels(word):
    return numVowels(word)/float(len(word))

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
    # print propVowels("APPLE")
