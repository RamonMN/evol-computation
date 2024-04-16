import random
from cost_functions import cost_function, interpolate

def get_fitness(individual):

    chromossome_size = int(len(individual)/2)

    x1_bin = individual[0:chromossome_size]
    x2_bin = individual[chromossome_size:]

    fitness = cost_function(x1_bin, x2_bin)

    return fitness


def select(population, method, elitsm):
    population_selected = []
    population_size = len(population)

    if (method == "tournament"):
        for _ in range(population_size):
            index_1 = random.randint(0, (population_size-1))
            index_2 = random.randint(0, (population_size-1))

            candidate_1 = population[index_1]
            candidate_2 = population[index_2]

            candidate_1_fitness = get_fitness(candidate_1)
            candidate_2_fitness = get_fitness(candidate_2)

            if (candidate_1_fitness <= candidate_2_fitness):
                population_selected.append(candidate_1)
            else:
                population_selected.append(candidate_2)

    elif (method == "roullete"):
        population_selected = population


    return population_selected


def cross(population, probability):
    crossed_population = []

    # Iterate through pairs on population
    for i in range(0, len(population), 2):

        # Decide if they will be crossed
        if (random.random() <= probability):
            
            # Take the two individuals
            first_parent = population[i]
            second_parent = population[i + 1]
            
            chromossome_size = int(len(first_parent)/2)

            # Pick two random cut points
            first_cut = random.randint(0, (chromossome_size - 1))
            second_cut = random.randint(chromossome_size, ((chromossome_size*2) - 1))

            # Cross the parents
            first_child = first_parent[0:first_cut] + second_parent[first_cut:chromossome_size] + first_parent[chromossome_size:second_cut] + second_parent[second_cut:]
            second_child = second_parent[0:first_cut] + first_parent[first_cut:chromossome_size] + second_parent[chromossome_size:second_cut] + first_parent[second_cut:]

            # Save the children
            crossed_population.append(first_child)
            crossed_population.append(second_child)

        else:
            crossed_population.append(population[i])
            crossed_population.append(population[i+1])

    return crossed_population


def mutate(population, probability):
    mutated_population = []

    for individual in population:
        
        mutated_individual = []
        for bit in individual:
            if (random.random() <= probability): 
                if (bit == '0'):
                    mutated_individual.append('1')
                else:
                    mutated_individual.append('0')
            else:
                mutated_individual.append(bit)

        mutated_population.append("".join(mutated_individual))

    return mutated_population


if __name__ == '__main__':
    pass