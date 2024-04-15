import random
from costFunctions import deJong5, ellipticParaboloid


# Takes a binary value (list) and its limits (decimals) to interpolate into a decimal value.
def getRealValue(binaryValue, infLim, supLim):
    
    size = len(binaryValue)    
    resolution = (supLim - infLim)/((2**size) - 1)

    # Take the supplied list, convert into a string of 0's and 1's, and then convert to integer
    integerValue = int(''.join(str(bit) for bit in binaryValue), 2)

    return (infLim + integerValue*resolution)


def selectTournament(population):
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
        x1 = getRealValue(samples[0][:15], -65.536, 65.536)
        x2 = getRealValue(samples[0][15:], -65.536, 65.536)

        # Quality of first sample
        #sampleQuality1 = deJong5(x1, x2)
        sampleQuality1 = ellipticParaboloid(x1, x2)

        # Converting second individual genes into real values to evaluate fitness
        x1 = getRealValue(samples[1][:15], -65.536, 65.536)
        x2 = getRealValue(samples[1][15:], -65.536, 65.536)

        # Quality of second sample
        #sampleQuality2 = deJong5(x1, x2)      
        sampleQuality2 = ellipticParaboloid(x1, x2)

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


def selectRoullete(population):
    pass

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
            firstCut = random.randint(5, 14)
            
            auxVariable = firstIndividual

            firstIndividual[firstCut:15] = secondIndividual[firstCut:15]
            secondIndividual[firstCut:15] = auxVariable[firstCut:15]

            # Pick random cut point for the second chromossome
            secondCut = random.randint(20, 29)

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
            randomBit = random.randint(0, 29)
            
            # Flip the gene
            mutatedIndividual[randomBit] = int(not mutatedIndividual[randomBit])

            # Save the mutated individual
            mutatedPopulation.append(mutatedIndividual)

        else:
            mutatedPopulation.append(population[i])

    return mutatedPopulation


if __name__ == '__main__':
    getRealValue([0, 0, 0, 0, 0, 0, 0, 0, 1, 1], -10.0, 10.0)