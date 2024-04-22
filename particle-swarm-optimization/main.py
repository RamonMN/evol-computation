import random
from costFunctions import costFunction
import matplotlib.pyplot as plt

class Particle():
    def __init__(self, x, v, xRange, vRange):
        # Since we are working with two dimensional functions,
        # we can see the x[0] as the x axis and the x[1] as the y axis,
        # in the cartesian plane
        self.x = x
        self.v = v

        self.xRange = xRange
        self.vRange = vRange
        
        self.particleBestPosition = self.x
        self.particleBestValue = costFunction(self.particleBestPosition)

    def saturatePosition(self):
        # Check if x exceeds the left border
        if self.x[0] < self.xRange[0]:
            self.x[0] = self.xRange[0]
            self.v[0] = 0.0

        # Check if x exceeds the right border
        if self.x[0] > self.xRange[1]:
            self.x[0] = self.xRange[1]
            self.v[0] = 0.0

        # Check if x exceeds the bottom border
        if self.x[1] < self.xRange[0]:
            self.x[1] = self.xRange[0]
            self.v[1] = 0.0

        # Check if x exceeds the top border
        if self.x[1] > self.xRange[1]:
            self.x[1] = self.xRange[1]
            self.v[1] = 0.0       

    def saturateVelocity(self):

        if self.v[0] < self.vRange[0]:
            self.v[0] = self.vRange[0]
        
        if self.v[0] > self.vRange[1]:
            self.v[0] = self.vRange[1]
        
        if self.v[1] < self.vRange[0]:
            self.v[0] = self.vRange[0]

        if self.v[1] > self.vRange[1]:
            self.v[1] = self.vRange[1]


class Population():
    def __init__(self, populationSize, xRange, vRange, w, c1, c2):
        self.population = []
        
        self.populationSize = populationSize
        self.xRange = xRange
        self.vRange = vRange

        self.w = w
        self.c1 = c1
        self.c2 = c2

        self.globalBestPosition = [0.0, 0.0]
        self.globalBestValue = costFunction(self.globalBestPosition)

        self.initializePopulation()

    def initializePopulation(self):
        for i in range(self.populationSize):           
            # Take random values between xMin and xMax
            x1 = self.xRange[0] + random.random()*(self.xRange[1] - self.xRange[0])
            x2 = self.xRange[0] + random.random()*(self.xRange[1] - self.xRange[0])
            x = [x1, x2]

            # Take random values between vMin and vMax
            v1 = self.vRange[0] + random.random()*(self.vRange[1] - self.vRange[0])
            v2 = self.vRange[0] + random.random()*(self.vRange[1] - self.vRange[0])
            v = [v1, v2]

            self.population.append(Particle(x, v, self.xRange, self.vRange))

    def updatePopulation(self):

        for particle in self.population:
            
            particleValue = costFunction(particle.x)

            if (particleValue < particle.particleBestValue):
                particle.particleBestPosition = particle.x
                particle.particleBestValue = particleValue
                
                if (particleValue < self.globalBestValue):
                    self.globalBestPosition = particle.x
                    self.globalBestValue = particleValue

            # Update the two velocities
            r1 = random.random()
            r2 = random.random()

            particle.v[0] = self.w*particle.v[0] + self.c1*r1*(particle.particleBestPosition[0] - particle.x[0]) + self.c2*r2*(self.globalBestPosition[0] - particle.x[0])

            r1 = random.random()
            r2 = random.random()

            particle.v[1] = self.w*particle.v[1] + self.c1*r1*(particle.particleBestPosition[1] - particle.x[1]) + self.c2*r2*(self.globalBestPosition[1] - particle.x[1])

            # Saturate velocity between vmin and vmax
            particle.saturateVelocity()

            # Update the two positions
            particle.x[0] = particle.x[0] + particle.v[0]
            particle.x[1] = particle.x[1] + particle.v[1]
            
            # Saturate positions
            particle.saturatePosition()


if __name__ == '__main__':



    pop = Population(1000, [-65.536, 65.536], [-0.05, 0.05], 0.7, 2.05, 2.05)

    nEpochs = 100

    for i in range(nEpochs):
        pop.updatePopulation()
        
        print(pop.globalBestValue)

        #X = []
        #Y = []
        #for particle in pop.population:
        #    X.append(particle.x[0])
        #    Y.append(particle.x[1])

        #plt.figure()
        #plt.scatter(X, Y)
        

    #plt.show()