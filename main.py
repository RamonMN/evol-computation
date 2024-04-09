import numpy as np
import random
import matplotlib.pyplot as plt

#random.seed(0)

def deJong5(x1, x2):
    a1 = [-32, -16, 0, 16, 32]*5
    a2 = [-32]*5 + [-16]*5 + [0]*5 + [16]*5 + [32]*5
    a = [a1, a2]

    sum = 0.002
    for i in range(1, 26):
        sum += ( 1 / (i + (x1 - a[0][i-1])**6 + (x2 - a[1][i-1])**6) )

    # The function actually should return 1/sum, but we want to evaluate the min value,
    # so we will return sum and try to finding the max value.
    # This will simplify the implementation of the roulette method.
    return sum

def getRealValue(intValue, size, infLim, supLim):
    resolution = (supLim - infLim)/((2**size) - 1)

    return infLim + intValue*resolution

def selectPopulationTournament(population):
    bestIndividual = 0
    bestQuality = 0
    populationSelected = []

    # It will take two random samples from population and keep the best until complete population size
    for i in range(len(population)):

        # Taking two random index
        index1 = random.randint(0, len(population)-1)
        index2 = random.randint(0, len(population)-1)

        # Taking samples from population
        samples = [population[index1], population[index2]]

        # Converting first individual genes into real values to evaluate fitness
        x1_int = int(''.join(str(gene) for gene in samples[0][:10]), 2)
        x2_int = int(''.join(str(gene) for gene in samples[0][10:]), 2)
        x1_real = getRealValue(x1_int, 10, -65.536, 65.536)
        x2_real = getRealValue(x2_int, 10, -65.536, 65.536)

        # Quality of first sample
        sampleQuality1 = deJong5(x1_real, x2_real)

        # Converting second individual genes into real values to evaluate fitness
        x1_int = int(''.join(str(gene) for gene in samples[1][:10]), 2)
        x2_int = int(''.join(str(gene) for gene in samples[1][10:]), 2)
        x1_real = getRealValue(x1_int, 10, -65.536, 65.536)
        x2_real = getRealValue(x2_int, 10, -65.536, 65.536)

        # Quality of second sample
        sampleQuality2 = deJong5(x1_real, x2_real)      

        if (sampleQuality1 >= sampleQuality2):
            if (sampleQuality1 >= bestQuality):
                bestQuality = sampleQuality1
                bestIndividual = samples[0]
            populationSelected.append(samples[0])
        else:
            if (sampleQuality2 >= bestQuality):
                bestQuality = sampleQuality2
                bestIndividual = samples[1]
            populationSelected.append(samples[1])

    return (populationSelected, bestIndividual, bestQuality)

def crossover(population):
    crossedPopulation = []

    for i in range(0, len(population), 2):
        firstIndividual = population[i]
        secondIndividual = population[i + 1]

        



    pass

populationSize = 100
chromossomeSize = 20
geneRanges = [(-65.536, 65.536), (-65.536, 65.536)]
numberOfEpochs = 100
crossoverProbability = 0.8
mutationProbability = 0.1


population = [[0 for i in range(chromossomeSize)] for j in range(populationSize)]
bestIndividuals = []
bestQualities = []

# Initialize population
for i in range(populationSize):
    for j in range(chromossomeSize):
        if (random.random() >= 0.5):
            population[i][j] = 1

epoch = 0
while (epoch < numberOfEpochs):

    (population, bestIndividual, bestQuality) = selectPopulationTournament(population)

    bestIndividuals.append(bestIndividual)
    bestQualities.append(bestQuality)





    epoch += 1

print(bestQualities)