import numpy as np
import matplotlib.pyplot as pyplot
from ypstruct import structure
import GA

# Sphere Test Function
def Sphere(x):
    sum = 0
    for i in x:
        sum += i**2
    return sum


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
params.npop = 20


# Run GA
out = GA.run(problem, params)