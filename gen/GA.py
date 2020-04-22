from ypstruct import structure
import numpy as np

def run(problem, param):
    
    # Problem information
    costFunction = problem.costFunction
    nvar = problem.nvar
    varmax = problem.varmax
    varmin = problem.varmin

    # Parameters
    maxit = param.maxit
    npop = param.npop

    # Empty population template
    empty_pop_temp = structure()
    empty_pop_temp.position = None
    empty_pop_temp.cost = None

    # Best solution in initial population
    bestSol = empty_pop_temp.deepcopy()
    bestSol.cost = np.inf

    # Initial Population
    pop = empty_pop_temp.repeat(npop)


    for i in range(npop):
        pop[i].position = np.random.uniform(varmin, varmax, nvar)
        pop[i].cost = costFunction(pop[i].position)

        if pop[i].cost < bestSol.cost:
            bestSol = pop[i].deepcopy()

    # print(bestSol.position)
    # print(bestSol.cost)

    out = structure()
    out.pop = pop

    return out