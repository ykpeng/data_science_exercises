# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """

    pylab.subplot(221)
    simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005, numTrials, 150)
    pylab.subplot(222)
    simulationWithDrug(150, 1000, 0.1, 0.05, {'guttagonol': False }, 0.005, numTrials, 150)
    # pylab.subplot(223)
    # simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005, numTrials, 75)
    # pylab.subplot(224)
    # simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005, numTrials, 0)
    pylab.show()

def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials, delay):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1).
    numTrials: number of simulation runs to execute (an integer)

    """
    lastPopSizes = []
    for i in range(numTrials):
        lastPopSize = simulationOneTrial(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, delay)
        lastPopSizes.append(lastPopSize)
    renderPlot(lastPopSizes, delay)

def simulationOneTrial(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, delay):
    viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for i in range(numViruses)]
    patient = TreatedPatient(viruses, maxPop)
    lastPopSize = numViruses
    for i in range(delay):
        lastPopSize = patient.update()
    patient.addPrescription("guttagonol")
    for i in range(150):
        lastPopSize = patient.update()
    return lastPopSize

def renderPlot(vals, delay):
    pylab.hist(vals, bins=12, range=(0,600))
    pylab.title(delay)
    pylab.xlabel("final virus population")
    pylab.ylabel("number trials")
    # pylab.show()

# simulationDelayedTreatment(100)
#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    pylab.subplot(221)
    simulationWithDrug(100, 1000, 0.1, 0.05,  {'guttagonol': False, 'grimpex': False}, 0.005, numTrials, 300)
    pylab.subplot(222)
    simulationWithDrug(100, 1000, 0.1, 0.05,  {'guttagonol': False, 'grimpex': False}, 0.005, numTrials, 150)
    pylab.subplot(223)
    simulationWithDrug(100, 1000, 0.1, 0.05,  {'guttagonol': False, 'grimpex': False}, 0.005, numTrials, 75)
    pylab.subplot(224)
    simulationWithDrug(100, 1000, 0.1, 0.05,  {'guttagonol': False, 'grimpex': False}, 0.005, numTrials, 0)
    pylab.show()

def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials, delay):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1).
    numTrials: number of simulation runs to execute (an integer)

    """
    lastPopSizes = []
    for i in range(numTrials):
        lastPopSize = simulationOneTrial2(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, delay)
        lastPopSizes.append(lastPopSize)
    renderPlot(lastPopSizes, delay)

def simulationOneTrial2(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, delay):
    viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for i in range(numViruses)]
    patient = TreatedPatient(viruses, maxPop)
    lastPopSize = numViruses
    for i in range(150):
        lastPopSize = patient.update()
    patient.addPrescription("guttagonol")
    for i in range(delay):
        lastPopSize = patient.update()
    patient.addPrescription("grimpex")
    for i in range(150):
        lastPopSize = patient.update()
    return lastPopSize

simulationTwoDrugsDelayedTreatment(100)
