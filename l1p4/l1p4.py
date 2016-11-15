import pylab
import numpy as np

def loadFile():
    inFile = open('julyTemps.txt')

    highTemps = []
    lowTemps = []

    for line in inFile:
        fields = line.split()
        if len(fields) < 3 or not fields[0].isdigit():
            continue
        else:
            highTemps.append(int(fields[1]))
            lowTemps.append(int(fields[2]))
    return (lowTemps, highTemps)

def producePlot(lowTemps, highTemps):
    # diffTemps = []
    # for i in range(31):
    #     diff = highTemps[i] - lowTemps[i]
    #     diffTemps.append(diff)
    diffTemps = list(np.array(highTemps) - np.array(lowTemps))

    pylab.plot(range(1, 32), diffTemps)
    pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
    pylab.xlabel('Days')
    pylab.ylabel('Temperature Ranges')
    pylab.show()

(lowTemps, highTemps) = loadFile()
producePlot(lowTemps, highTemps)
