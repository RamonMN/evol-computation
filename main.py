import matplotlib.pyplot as plt
import random
from geneticAlgorithm import selectTournament, crossover, mutation

populationSize = 80
chromossomeSize = 30
numberOfEpochs = 100
crossoverProbability = 0.8
mutationProbability = 0.02
bestIndividuals = []
bestQualities = []

# Initialize population
population = [[round(random.random()) for i in range(chromossomeSize)] for j in range(populationSize)]

for epoch in range(numberOfEpochs):

    # Select
    (population, bestIndividual, bestQuality) = selectTournament(population)
    
    # Crossover
    population = crossover(population, crossoverProbability)
    
    # Mutation
    population = mutation(population, mutationProbability)

    # Save best individuals to future analysis
    bestIndividuals.append(bestIndividual)
    bestQualities.append(bestQuality)


print(min(bestQualities))
plt.plot(bestQualities)
plt.show()
