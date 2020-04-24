import numpy as np
import matplotlib.pyplot as plt
from ypstruct import structure
import GA

WeightPerPosotion = [1000, -25, 625, -25, 100, -25, 25, -25, 205, -25, 250, -25]

# Sphere Test Function
def Sphere(x):
    Sum = 0
    for i in range(12):
        if x[i] == 1:
            Sum += WeightPerPosotion[i]
    return Sum


# Problem Defination
problem = structure()
problem.costFunction = Sphere
problem.nvar = 12
problem.varmin = 0
problem.varmax = 1


# GA Parameters
params = structure()
params.cost = Sphere
params.maxit = 50
params.npop = 40   # Initial number of offspring
params.pc = 2       # Proportional of offspring
params.mu = 0.4       # Mutation parameter
params.beta = 1     # Parent selection parameter


# Run GA
out = GA.run(problem, params)

# Result
x = [i for i in range(params.maxit)]
y = [out.bestSolution[j].cost for j in range(len(out.bestSolution))]

plt.plot(x, y, 'r')
plt.xlabel('Iteration')
plt.ylabel('Best Cost')
plt.title('Genetic Algorithm output curve')
plt.grid(True)
plt.show()