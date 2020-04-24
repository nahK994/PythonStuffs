from ypstruct import structure
import numpy as np

def run(problem, params):
    
    # Problem information
    costFunction = problem.costFunction
    nvar = problem.nvar
    varmax = problem.varmax
    varmin = problem.varmin

    # Parameters
    maxit = params.maxit
    npop = params.npop
    gamma = params.gamma
    mu = params.mu
    sigma = params.sigma
    pc = params.pc
    nc = np.round(pc*npop/2)*2
    beta = params.beta

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

    bestSolution = empty_pop_temp.repeat(maxit)
    # print(bestSolution)

    for it in range(maxit):

        costs = np.array([x.cost for x in pop])
        avg_cost = np.mean(costs)
        if avg_cost != 0:
            costs /= avg_cost
        probability = np.exp(-beta*costs)

        popc = []
        for k in range(int(nc/2)):

            # Parant selection
            # q = np.random.permutation(npop)
            # p1 = pop[q[0]]
            # p2 = pop[q[1]]
            p1 = pop[wheel_selection(probability)]
            p2 = pop[wheel_selection(probability)]

            # Crossover
            c1, c2 = crossover(p1, p2, gamma)

            # Mutation
            c1 = mutation(c1, mu, sigma)
            c2 = mutation(c2, mu, sigma)

            # Apply bounds
            c1 = apply_bounds(c1, varmax, varmin)
            c2 = apply_bounds(c2, varmax, varmin)

            # Evaluation
            c1.cost = costFunction(c1.position)
            if c1.cost < bestSol.cost:
                bestSol = c1.deepcopy()

            c2.cost = costFunction(c2.position)
            if c2.cost < bestSol.cost:
                bestSol = c2.deepcopy()

            # Storing offsprings
            popc.append(c1)
            popc.append(c2)

        # Adding, Sorting, Marging....
        pop += popc
        sorted(pop, key = lambda x: x.cost)
        pop = pop[0: npop]

        # Best solution per iterations
        bestSolution[it].cost = bestSol.cost
        bestSolution[it].position = bestSol.position
        
        print('Iteration %d: bestSolution = %d' %(it, bestSolution[it].cost))
        print(bestSolution[it].position)
        print()


    out = structure()
    out.pop = pop
    out.bestSol = bestSol
    out.bestSolution = bestSolution
    return out


def crossover(c1, c2, gamma):

    a1 = c1.deepcopy()
    a2 = c2.deepcopy()
    alpha = np.random.uniform(-gamma, 1+gamma, *c1.position.shape)

    c1.position = alpha*a1.position + (1-alpha)*a2.position
    c2.position = alpha*a1.position + (1-alpha)*a1.position

    return c1, c2


def mutation(x, mu, sigma):

    y = x.deepcopy()

    flag = np.random.rand(*x.position.shape) <= mu
    ind = np.argwhere(flag)

    y.position[ind] += sigma*np.random.randn(*ind.shape)
    return y


def apply_bounds(x, varmax, varmin):

    x.position = np.maximum(x.position, varmin)
    x.position = np.minimum(x.position, varmax)
    return x


def wheel_selection(p):

    s = np.sum(p)
    c = np.cumsum(p)
    flag = s*np.random.rand() <= c
    ind = np.argwhere(flag)
    return ind[0][0]