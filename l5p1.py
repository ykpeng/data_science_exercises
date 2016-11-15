def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    num_all_same = [allSameColor() for i in numTrials]
    return sum(num_all_same) / numTrials

def allSameColor():
    balls = ["R","R","R","G","G","G"]
    last_drawn = None
    for i in range(3):
        ball = random.choice(balls)
        if last_drawn and last_drawn != ball:
            return False
        last_drawn = ball
        balls.remove(ball)
    return True
