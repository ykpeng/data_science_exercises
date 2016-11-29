import random, pylab

def p3():
    xVals = []
    yVals = []
    wVals = []
    for i in range(1000):
        xVals.append(random.random())
        yVals.append(random.random())
        wVals.append(random.random())
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    wVals = pylab.array(wVals)
    xVals = xVals + xVals
    zVals = xVals + yVals
    tVals = xVals + yVals + wVals

    # pylab.hist(xVals)
    # pylab.hist(yVals)
    # pylab.hist(zVals)
    pylab.hist(tVals)
    pylab.show()

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3
    balls of the same color were drawn in the first 3 draws.
    '''
    results = []
    for i in range(numTrials):
        results.append(drawThree())
    return sum(results) / float(numTrials)

def drawThree():
    last = None
    balls = ["R", "R", "R", "R", "G", "G", "G", "G"]
    for i in range(3):
        drawn = random.choice(balls)
        if last != None and drawn != last:
            return False
        else:
            last = drawn
            balls.remove(drawn)
    return True

print drawing_without_replacement_sim(1000)
