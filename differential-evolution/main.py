import random


population_size = 100
crossing_rate = 0.2
F = 0.3
x_size = 2
x_range = [-65.536, 65.536]

population = [[random.uniform(x_range[0], x_range[1]) for j in range(x_size)] for i in range(population_size)]

for index, x_i in enumerate(population[:]):
    index_1 = random.randint(0, population_size-1)
    index_2 = random.randint(0, population_size-1)
    index_3 = random.randint(0, population_size-1)

    x_r_1 = population[index_1]
    x_r_2 = population[index_2]
    x_r_3 = population[index_3]

    v_i = [ (x_r_1[j] + F*(x_r_3[j] - x_r_2[j])) for j in range(x_size)]
    


