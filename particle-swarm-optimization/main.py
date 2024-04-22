import random
from math import sqrt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import pandas as pd
from costFunctions import deJong5, langermann

def saturate(value, range):
    returnValue = 0.0
    if value < range[0]:
        returnValue = range[0]
    elif value > range[1]:
        returnValue = range[1]
    else:
        returnValue = value

    return returnValue


class Particle():
    def __init__(self, x, v, costFunction):
        self.x = x
        self.v = v
        self.costFunction = costFunction

        self.particleBestPosition = self.x
        self.particleBestValue = self.costFunction(self.particleBestPosition)   


class Population():
    def __init__(self, costFunction, populationSize, particleSize, xRange, vRange, w, c1, c2):
        self.population = []
        
        self.populationSize = populationSize
        self.particleSize = particleSize
        self.xRange = xRange
        self.vRange = vRange

        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.costFunction = costFunction

        self.globalBestPosition = [0.0]*self.particleSize
        self.globalBestValue = self.costFunction(self.globalBestPosition)

        self.initializePopulation()

    def initializePopulation(self):
        for i in range(self.populationSize):  
            x = []
            v = []
            for j in range(self.particleSize):
                x.append(random.uniform(self.xRange[0], self.xRange[1]))
                v.append(random.uniform(self.vRange[0], self.vRange[1])) 

            self.population.append(Particle(x, v, self.costFunction))

    def updatePopulation(self, updateMethod, epoch, maxEpochs):

        for particle in self.population:
            
            particleValue = self.costFunction(particle.x)

            if (particleValue < particle.particleBestValue):
                particle.particleBestPosition = particle.x
                particle.particleBestValue = particleValue
                
                if (particleValue < self.globalBestValue):
                    self.globalBestPosition = particle.x
                    self.globalBestValue = particleValue

            for j in range(self.particleSize):
                # Update the two velocities
                r1 = random.random()
                r2 = random.random()

                if (updateMethod == "default"):
                    particle.v[j] = self.w*particle.v[j] + self.c1*r1*(particle.particleBestPosition[j] - particle.x[j]) + self.c2*r2*(self.globalBestPosition[j] - particle.x[j])
                    particle.v[j] = saturate(particle.v[j], self.vRange)

                    particle.x[j] = particle.x[j] + particle.v[j]
                    particle.x[j] = saturate(particle.x[j], self.xRange)

                elif (updateMethod == "inertia"):
                    wMax = 0.9
                    wMin = 0.4

                    currW = wMax - epoch * ((wMax - wMin)/(maxEpochs))

                    particle.v[j] = currW*particle.v[j] + self.c1*r1*(particle.particleBestPosition[j] - particle.x[j]) + self.c2*r2*(self.globalBestPosition[j] - particle.x[j])
                    particle.v[j] = saturate(particle.v[j], self.vRange)

                    particle.x[j] = particle.x[j] + particle.v[j]
                    particle.x[j] = saturate(particle.x[j], self.xRange)

                elif (updateMethod == "constriction"):
                    phi = self.c1 + self.c2
                    kappa = 1.0
                    chi = (2*kappa) / (abs(2.0 - phi - sqrt((phi**2) - 4*phi)))

                    particle.v[j] = chi*(particle.v[j] + self.c1*r1*(particle.particleBestPosition[j] - particle.x[j]) + self.c2*r2*(self.globalBestPosition[j] - particle.x[j]))
                    particle.v[j] = saturate(particle.v[j], self.vRange)

                    particle.x[j] = particle.x[j] + particle.v[j]
                    particle.x[j] = saturate(particle.x[j], self.xRange)



# Fixed parameters
particleSize = 2
w = 0.7
c1 = 2.05
c2 = 2.05
vRange = [-0.1, 0.1]
xRangeDejong5 = [-65.536, 65.536]
xRangeLangermann = [-10.0, 10.0]

#cost = deJong5
#populationSize = 200
#nEpochs = 100
#method = "constriction"

configs = [{"cost": deJong5, "xRange": xRangeDejong5, "method": "default", "popSize": 50, "nEpochs": 50},
           {"cost": deJong5, "xRange": xRangeDejong5, "method": "default", "popSize": 200, "nEpochs": 50},
           {"cost": deJong5, "xRange": xRangeDejong5, "method": "default", "popSize": 800, "nEpochs": 50},
           {"cost": deJong5, "xRange": xRangeDejong5, "method": "default", "popSize": 50, "nEpochs": 100},
           {"cost": deJong5, "xRange": xRangeDejong5, "method": "default", "popSize": 200, "nEpochs": 100},
           {"cost": deJong5, "xRange": xRangeDejong5, "method": "default", "popSize": 800, "nEpochs": 100},
           {"cost": deJong5, "xRange": xRangeDejong5, "method": "default", "popSize": 50, "nEpochs": 150},
           {"cost": deJong5, "xRange": xRangeDejong5, "method": "default", "popSize": 200, "nEpochs": 150},
           {"cost": deJong5, "xRange": xRangeDejong5, "method": "default", "popSize": 800, "nEpochs": 150},
           {"cost": deJong5, "xRange": xRangeDejong5, "method": "constriction", "popSize": 50, "nEpochs": 50},
           {"cost": deJong5, "xRange": xRangeDejong5, "method": "constriction", "popSize": 200, "nEpochs": 50},
           {"cost": deJong5, "xRange": xRangeDejong5, "method": "constriction", "popSize": 800, "nEpochs": 50},
           {"cost": deJong5, "xRange": xRangeDejong5, "method": "constriction", "popSize": 50, "nEpochs": 100},
           {"cost": deJong5, "xRange": xRangeDejong5, "method": "constriction", "popSize": 200, "nEpochs": 100},
           {"cost": deJong5, "xRange": xRangeDejong5, "method": "constriction", "popSize": 800, "nEpochs": 100},
           {"cost": deJong5, "xRange": xRangeDejong5, "method": "constriction", "popSize": 50, "nEpochs": 150},
           {"cost": deJong5, "xRange": xRangeDejong5, "method": "constriction", "popSize": 200, "nEpochs": 150},
           {"cost": deJong5, "xRange": xRangeDejong5, "method": "constriction", "popSize": 800, "nEpochs": 150},
           {"cost": deJong5, "xRange": xRangeDejong5, "method": "inertia", "popSize": 50, "nEpochs": 50},
           {"cost": deJong5, "xRange": xRangeDejong5, "method": "inertia", "popSize": 200, "nEpochs": 50},
           {"cost": deJong5, "xRange": xRangeDejong5, "method": "inertia", "popSize": 800, "nEpochs": 50},
           {"cost": deJong5, "xRange": xRangeDejong5, "method": "inertia", "popSize": 50, "nEpochs": 100},
           {"cost": deJong5, "xRange": xRangeDejong5, "method": "inertia", "popSize": 200, "nEpochs": 100},
           {"cost": deJong5, "xRange": xRangeDejong5, "method": "inertia", "popSize": 800, "nEpochs": 100},
           {"cost": deJong5, "xRange": xRangeDejong5, "method": "inertia", "popSize": 50, "nEpochs": 150},
           {"cost": deJong5, "xRange": xRangeDejong5, "method": "inertia", "popSize": 200, "nEpochs": 150},
           {"cost": deJong5, "xRange": xRangeDejong5, "method": "inertia", "popSize": 800, "nEpochs": 150},
           {"cost": langermann, "xRange": xRangeLangermann, "method": "default", "popSize": 50, "nEpochs": 50},
           {"cost": langermann, "xRange": xRangeLangermann, "method": "default", "popSize": 200, "nEpochs": 50},
           {"cost": langermann, "xRange": xRangeLangermann, "method": "default", "popSize": 800, "nEpochs": 50},
           {"cost": langermann, "xRange": xRangeLangermann, "method": "default", "popSize": 50, "nEpochs": 100},
           {"cost": langermann, "xRange": xRangeLangermann, "method": "default", "popSize": 200, "nEpochs": 100},
           {"cost": langermann, "xRange": xRangeLangermann, "method": "default", "popSize": 800, "nEpochs": 100},
           {"cost": langermann, "xRange": xRangeLangermann, "method": "default", "popSize": 50, "nEpochs": 150},
           {"cost": langermann, "xRange": xRangeLangermann, "method": "default", "popSize": 200, "nEpochs": 150},
           {"cost": langermann, "xRange": xRangeLangermann, "method": "default", "popSize": 800, "nEpochs": 150},
           {"cost": langermann, "xRange": xRangeLangermann, "method": "constriction", "popSize": 50, "nEpochs": 50},
           {"cost": langermann, "xRange": xRangeLangermann, "method": "constriction", "popSize": 200, "nEpochs": 50},
           {"cost": langermann, "xRange": xRangeLangermann, "method": "constriction", "popSize": 800, "nEpochs": 50},
           {"cost": langermann, "xRange": xRangeLangermann, "method": "constriction", "popSize": 50, "nEpochs": 100},
           {"cost": langermann, "xRange": xRangeLangermann, "method": "constriction", "popSize": 200, "nEpochs": 100},
           {"cost": langermann, "xRange": xRangeLangermann, "method": "constriction", "popSize": 800, "nEpochs": 100},
           {"cost": langermann, "xRange": xRangeLangermann, "method": "constriction", "popSize": 50, "nEpochs": 150},
           {"cost": langermann, "xRange": xRangeLangermann, "method": "constriction", "popSize": 200, "nEpochs": 150},
           {"cost": langermann, "xRange": xRangeLangermann, "method": "constriction", "popSize": 800, "nEpochs": 150},
           {"cost": langermann, "xRange": xRangeLangermann, "method": "inertia", "popSize": 50, "nEpochs": 50},
           {"cost": langermann, "xRange": xRangeLangermann, "method": "inertia", "popSize": 200, "nEpochs": 50},
           {"cost": langermann, "xRange": xRangeLangermann, "method": "inertia", "popSize": 800, "nEpochs": 50},
           {"cost": langermann, "xRange": xRangeLangermann, "method": "inertia", "popSize": 50, "nEpochs": 100},
           {"cost": langermann, "xRange": xRangeLangermann, "method": "inertia", "popSize": 200, "nEpochs": 100},
           {"cost": langermann, "xRange": xRangeLangermann, "method": "inertia", "popSize": 800, "nEpochs": 100},
           {"cost": langermann, "xRange": xRangeLangermann, "method": "inertia", "popSize": 50, "nEpochs": 150},
           {"cost": langermann, "xRange": xRangeLangermann, "method": "inertia", "popSize": 200, "nEpochs": 150},
           {"cost": langermann, "xRange": xRangeLangermann, "method": "inertia", "popSize": 800, "nEpochs": 150}
           ]


bestPerConfig = []
for i in range(len(configs)):

    print(f"config {i}...")

    bestParticles = []
    for j in range(30):
        pop = Population(configs[i]["cost"], configs[i]["popSize"], particleSize, configs[i]["xRange"], vRange, w, c1, c2)

        for epoch in range(configs[i]["nEpochs"]):

            pop.updatePopulation(configs[i]["method"], epoch, configs[i]["nEpochs"])
        
        bestParticles.append(pop.globalBestValue)

    bestPerConfig.append(bestParticles)



bestConfigMedians = []
for i in bestPerConfig:
    bestConfigMedians.append(np.median(i))
    print(f"{np.mean(i)};{np.median(i)};{np.max(i)};{np.min(i)}")


bestConfigDejong = np.min(bestConfigMedians[0:27])
bestConfigDejongIndex = bestConfigMedians.index(bestConfigDejong)
print(f"best config dejong index: {bestConfigDejongIndex}")


bestConfigLangermann = np.min(bestConfigMedians[27:])
bestConfigLangermannIndex = bestConfigMedians.index(bestConfigLangermann)
print(f"best config langermann index: {bestConfigLangermannIndex}")


df = pd.DataFrame()

for i in range(len(bestPerConfig)):
    df[f"config{i}"] = bestPerConfig[i]

print(df.head())
df.to_csv("out.csv", sep=";", index=None)



"""
pop1 = Population(cost, populationSize, particleSize, xRangeDejong5, vRange, w, c1, c2)


for epoch in range(nEpochs):
    pop1.updatePopulation(method, epoch, nEpochs)

    print(pop1.globalBestValue)
"""

"""
X_c, Y_c = np.meshgrid(np.linspace(xRange[0], xRange[1], 200), np.linspace(xRange[0], xRange[1], 200))
Z_c = cost(X_c, Y_c)

X = []
Y = []
for particle in pop.population:
    X.append(particle.x[0])
    Y.append(particle.x[1])


fig, ax = plt.subplots()
ax.set_xlim(xRange)
ax.set_ylim(xRange)
ax.imshow(Z_c, extent=(X_c.min(), X_c.max(), Y_c.max(), Y_c.min()), interpolation='nearest')
scat = ax.scatter(X, Y, s=10, color='red')

def update(frame):
    pop.updatePopulation()
    print(pop.globalBestValue)
    
    X = []
    Y = []
    for particle in pop.population:
        X.append(particle.x[0])
        Y.append(particle.x[1])
    
    ax.cla()
    ax.set_xlim(xRange)
    ax.set_ylim(xRange)

    ax.imshow(Z_c, extent=(X_c.min(), X_c.max(), Y_c.max(), Y_c.min()), interpolation='nearest', cmap='gray')
    scat = ax.scatter(X, Y, s=10, color='red')


    return scat,

ani = animation.FuncAnimation(fig=fig, func=update, frames=40, interval=30)
plt.show()
"""

