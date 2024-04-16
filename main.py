import matplotlib.pyplot as plt
import random
from genetic_algorithm import select, cross, mutate, get_fitness

def get_best(generations):
    best_fitness_by_generation = []
    for population in generations:
        best = 10e6
        for individual in population:
            fitness = get_fitness(individual)

            if fitness <= best:
                best = fitness
        best_fitness_by_generation.append(best)

    return best_fitness_by_generation[-1]


population_size = 80
individual_size = 200
num_epochs= 150
cross_rate = 0.8
mutation_rate = 0.02

best_fitness_by_run = []

for _ in range(30):

    current_population = ["".join([str(round(random.random())) for i in range(individual_size)]) for j in range(population_size)]

    generations = []
    generations.append(current_population) # Save first population 

    for epoch in range(num_epochs):

        current_population = select(current_population, "tournament", False)

        current_population = cross(current_population, cross_rate)

        current_population = mutate(current_population, mutation_rate)

        generations.append(current_population) # Save current population

    best_fitness_by_run.append(get_best(generations))



plt.boxplot(best_fitness_by_run)
plt.show()



'''
for epoch in range(num_epochs):

    # Select
    population = select(population, "tournament")
    
    # Crossover
    population = cross(population, cross_rate)
    
    # Mutation
    population = mutate(population, mutation_rate)



print(min(bestQualities))
plt.plot(bestQualities)
plt.show()

'''
