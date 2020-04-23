import numpy as np
import matplotlib.pyplot as plt
from ypstruct import structure
import GA

# Sphere Test Function
def Sphere(x):
    return sum(x**4)


# Problem Defination
problem = structure()
problem.costFunction = Sphere
problem.nvar = 5
problem.varmin = -10
problem.varmax = 10


# GA Parameters
params = structure()
params.cost = Sphere
params.maxit = 100
params.npop = 500
params.pc = 4
params.gamma = 0.1  # Crossover parameter
params.mu = 1       # Mutation parameter
params.sigma = 0.5  # Mutation parameter


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