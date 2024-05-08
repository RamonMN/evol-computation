import random
import pandas as pd
from costFunctions import deJong5, langermann


def getBestFitness(population, costFunction):
    bestFitness = 1000000.0

    for i in range(len(population)):
        fitness = costFunction(population[i])

        if (fitness < bestFitness):
            bestFitness = fitness

    return bestFitness


def runDifferentialEvolution(costFunction, populationSize, indSize, indRange, F, crossRate, jumpRate, nEpochs):
    population_0 = [[random.uniform(indRange[0], indRange[1]) for j in range(indSize)] for i in range(populationSize)]

    # If opposition is enabled    
    if (jumpRate != None):
        oppPopulation_0 = [[(indRange[0] + indRange[1] - var) for var in ind] for ind in population_0]

        population = []
        for i in range(populationSize):
            if (costFunction(population_0[i]) < costFunction(oppPopulation_0[i])):
                population.append(population_0[i])
            else:
                population.append(oppPopulation_0[i])

        minRange = indRange[0]
        maxRange = indRange[1]

    # Otherwise
    else:
        population = population_0

    bestPerEpoch = []
    for _ in range(nEpochs):
        bestFitnessPerEpoch = getBestFitness(population, costFunction)
        bestPerEpoch.append(bestFitnessPerEpoch)

        for i in range(populationSize):

            x_i = population[i]
            x_i_Fitness = costFunction(x_i)

            index_1 = random.randint(0, populationSize-1)
            index_2 = random.randint(0, populationSize-1)
            index_3 = random.randint(0, populationSize-1)
            
            x_r_1 = population[index_1]
            x_r_2 = population[index_2]
            x_r_3 = population[index_3]

            indVariable = random.randint(0, indSize-1)

            trial = [0.0 for j in range(indSize)]
            for j in range(indSize):
                if ((random.random() <= crossRate) or (j == indVariable)):
                    trial[j] = x_r_1[j] + F*(x_r_2[j] - x_r_3[j])
                else:
                    trial[j] = x_i[j]
            
            trialFitness = costFunction(trial)

            if (trialFitness < x_i_Fitness):
                population[i] = trial

        # If opposition is enabled
        if (jumpRate != None):
            # Get new ranges
            for ind in population:
                for j in ind:
                    if j < minRange:
                        minRange = j
                    if j > maxRange:
                        maxRange = j    
                    
            for i in range(populationSize):

                if (random.random() <= jumpRate):
                    x_i = population[i]
                    x_opp = [(minRange + maxRange - j) for j in x_i]

                    x_i_Fitness = costFunction(x_i)
                    jumpTrialFitness = costFunction(x_opp)

                    if (jumpTrialFitness < x_i_Fitness):
                        population[i] = x_opp

        #print(getBestFitness(population, costFunction))

    bestFitness = getBestFitness(population, costFunction)

    return bestFitness, bestPerEpoch


configs = {"config1": [None, 0.25, 0.5, 50],
           "config2": [None, 0.25, 0.5, 100],
           "config3": [None, 0.25, 0.5, 200],
           "config4": [None, 0.25, 1.5, 50],
           "config5": [None, 0.25, 1.5, 100],
           "config6": [None, 0.25, 1.5, 200],
           "config7": [None, 0.75, 0.5, 50],
           "config8": [None, 0.75, 0.5, 100],
           "config9": [None, 0.75, 0.5, 200],
           "config10": [None, 0.75, 1.5, 50],
           "config11": [None, 0.75, 1.5, 100],
           "config12": [None, 0.75, 1.5, 200],
           "config13": [0.75, 0.25, 0.5, 50],
           "config14": [0.75, 0.25, 0.5, 100],
           "config15": [0.75, 0.25, 0.5, 200],
           "config16": [0.75, 0.25, 1.5, 50],
           "config17": [0.75, 0.25, 1.5, 100],
           "config18": [0.75, 0.25, 1.5, 200],
           "config19": [0.75, 0.75, 0.5, 50],
           "config20": [0.75, 0.75, 0.5, 100],
           "config21": [0.75, 0.75, 0.5, 200],
           "config22": [0.75, 0.75, 1.5, 50],
           "config23": [0.75, 0.75, 1.5, 100],
           "config24": [0.75, 0.75, 1.5, 200]    
}


deJong5Range = [-65.536, 65.536]
langRange = [-10.0, 10.0]

#dejongDF = pd.DataFrame()
#langDF = pd.DataFrame()

#for i in configs.keys():
#    print(f"\n{i} ...", end="")
#    
#    run = []
#    for _ in range(30):
#        print(f"{_} ", end="")

#        bestFitness = runDifferentialEvolution(deJong5, configs[i][3], 2, deJong5Range, configs[i][2], configs[i][1], configs[i][0], 100)
#        run.append(bestFitness)

#    dejongDF[i] = run

#dejongDF.to_csv("differential-evolution/dejong_configs.csv", sep=";", index=False)



#for i in configs.keys():
#    print(f"\n{i} ...", end="")
#    
#    run = []
#    for _ in range(30):
#        print(f"{_} ", end="")
#
#        bestFitness = runDifferentialEvolution(langermann, configs[i][3], 2, langRange, configs[i][2], configs[i][1], configs[i][0], 100)
#        run.append(bestFitness)

#    langDF[i] = run

#langDF.to_csv("differential-evolution/lang_configs.csv", sep=";", index=False)


bestFitness, bestFitnessPerEpochDejong = runDifferentialEvolution(deJong5, configs["config19"][3], 2, deJong5Range, configs["config19"][2], configs["config19"][1], configs["config19"][0], 100)

print(bestFitnessPerEpochDejong)
df1 = pd.DataFrame()
df1[f"dejong"] = bestFitnessPerEpochDejong
df1.to_csv("differential-evolution/de_dejong_best.csv", sep=";", index=None)


(bestFitness, bestFitnessPerEpochLang) = runDifferentialEvolution(langermann, configs["config19"][3], 2, langRange, configs["config19"][2], configs["config19"][1], configs["config19"][0], 100)

df2 = pd.DataFrame()
df2[f"lang"] = bestFitnessPerEpochLang
df2.to_csv("differential-evolution/de_lang_best.csv", sep=";", index=None)
