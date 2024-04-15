import numpy as np
import random
import matplotlib.pyplot as plt

#random.seed(0)

def deJong5(x1, x2):
    a1 = [-32.0, -16.0, 0.0, 16.0, 32.0]*5
    a2 = [-32.0]*5 + [-16.0]*5 + [0.0]*5 + [16.0]*5 + [32.0]*5
    a = [a1, a2]

    sum = 0.002
    for i in range(1, 26):
        sum += ( 1 / (i + (x1 - a[0][i-1])**6 + (x2 - a[1][i-1])**6) )
    
    return 1.0/sum

def getRealValue(intValue, size, infLim, supLim):
    resolution = (supLim - infLim)/((2**size) - 1)

    return infLim + intValue*resolution

def selectPopulationTournament(population):
    bestIndividual = 0
    bestQuality = 10e15
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

        if (sampleQuality1 <= sampleQuality2):
            populationSelected.append(samples[0])

            # Save the best individual for future analysis
            if (sampleQuality1 <= bestQuality):
                bestQuality = sampleQuality1
                bestIndividual = samples[0]
            
        else:
            populationSelected.append(samples[1])
            
            # Save the best individual for future analysis
            if (sampleQuality2 <= bestQuality):
                bestQuality = sampleQuality2
                bestIndividual = samples[1] 

    return (populationSelected, bestIndividual, bestQuality)


def crossover(population, probability):
    crossedPopulation = []

    # Iterate through pairs on population
    for i in range(0, len(population), 2):

        # Decide if they will be crossed
        if (random.random() <= probability):
            
            # Take the two individuals
            firstIndividual = population[i]
            secondIndividual = population[i + 1]

            # Pick random cut point for the first chromossome
            firstCut = random.randint(0, 9)
            
            auxVariable = firstIndividual

            firstIndividual[firstCut:10] = secondIndividual[firstCut:10]
            secondIndividual[firstCut:10] = auxVariable[firstCut:10]

            # Pick random cut point for the second chromossome
            secondCut = random.randint(10, 19)

            firstIndividual[secondCut:] = secondIndividual[secondCut:]
            secondIndividual[secondCut:] = auxVariable[secondCut:]
        
            # Substitute the parents with the crossed children
            crossedPopulation.append(firstIndividual)
            crossedPopulation.append(secondIndividual)
        else:
            crossedPopulation.append(population[i])
            crossedPopulation.append(population[i+1])

    return crossedPopulation


def mutation(population, probability):
    mutatedPopulation = []

    for i in range(len(population)):
        if (random.random() <= probability):
            # Take the individual to be mutated from population
            mutatedIndividual = population[i]

            # Take a random gene to flip
            randomBit = random.randint(0, 19)
            
            # Flip the gene
            mutatedIndividual[randomBit] = int(not mutatedIndividual[randomBit])

            # Save the mutated individual
            mutatedPopulation.append(mutatedIndividual)

        else:
            mutatedPopulation.append(population[i])

    return mutatedPopulation

populationSize = 500
chromossomeSize = 20
numberOfEpochs = 500
crossoverProbability = 0.8
mutationProbability = 0.1
bestIndividuals = []
bestQualities = []


# Initialize population
population = [[round(random.random()) for i in range(chromossomeSize)] for j in range(populationSize)]

epoch = 0
while (epoch < numberOfEpochs):

    (population, bestIndividual, bestQuality) = selectPopulationTournament(population)

    bestIndividuals.append(bestIndividual)
    bestQualities.append(bestQuality)

    population = crossover(population, crossoverProbability)
    population = mutation(population, mutationProbability)


    epoch += 1


plt.plot(bestQualities)
plt.show()


print(bestIndividuals)


#x1_int = int(''.join(str(gene) for gene in bestIndividuals[-1][:10]), 2)
#x2_int = int(''.join(str(gene) for gene in bestIndividuals[-1][10:]), 2)
#x1_real = getRealValue(x1_int, 10, -65.536, 65.536)
#x2_real = getRealValue(x2_int, 10, -65.536, 65.536)
#print(x1_real)
#print(x2_real)