import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from costFunctions import costFunction, deJong5, langermann

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
    def __init__(self, x, v):
        self.x = x
        self.v = v
     
        self.particleBestPosition = self.x
        self.particleBestValue = costFunction(self.particleBestPosition)   


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

        self.globalBestPosition = [0.0, 0.0]
        self.globalBestValue = self.costFunction(self.globalBestPosition)

        self.initializePopulation()

    def initializePopulation(self):
        for i in range(self.populationSize):  
            x = []
            v = []
            for j in range(self.particleSize):
                x.append(random.uniform(self.xRange[0], self.xRange[1]))
                v.append(random.uniform(self.vRange[0], self.vRange[1])) 

            self.population.append(Particle(x, v))

    def updatePopulation(self):

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

                particle.v[j] = self.w*particle.v[j] + self.c1*r1*(particle.particleBestPosition[j] - particle.x[j]) + self.c2*r2*(self.globalBestPosition[j] - particle.x[j])
                particle.v[j] = saturate(particle.v[j], self.vRange)

                particle.x[j] = particle.x[j] + particle.v[j]
                particle.x[j] = saturate(particle.x[j], self.xRange)



# Parameters
populationSize = 500
particleSize = 2
w = 0.7
c1 = 100.05
c2 = 0.05
nEpochs = 10

cost = deJong5
xRange = [-65.536, 65.536]
vRange = [-0.1, 0.1]




pop = Population(costFunction, populationSize, particleSize, xRange, vRange, w, c1, c2)

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

