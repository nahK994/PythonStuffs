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
    #sigma = params.sigma
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
        # pop[i].position = np.random.uniform(varmin, varmax, nvar)
        pop[i].position = np.random.randint(2, size=nvar)
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
            for i in range(len(costs)):
                costs[i] /= avg_cost
        probability = np.exp(-beta*costs)

        popc = []
        for k in range(int(nc/2)):

            # Parant selection
            p1 = pop[wheel_selection(probability)]
            p2 = pop[wheel_selection(probability)]

            # Crossover
            c1, c2 = crossover(p1, p2)


            # Mutation
            c11 = mutation(c1, mu)
            c22 = mutation(c2, mu)
            # c33 = mutation(c3, mu)
            # c44 = mutation(c4, mu)


            # Evaluation
            c1.cost = costFunction(c1.position)
            if c1.cost < bestSol.cost:
                bestSol = c1.deepcopy()

            c2.cost = costFunction(c2.position)
            if c2.cost < bestSol.cost:
                bestSol = c2.deepcopy()


            c11.cost = costFunction(c11.position)
            if c11.cost < bestSol.cost:
                bestSol = c11.deepcopy()

            c22.cost = costFunction(c22.position)
            if c22.cost < bestSol.cost:
                bestSol = c22.deepcopy()

            # c33.cost = costFunction(c33.position)
            # if c33.cost < bestSol.cost:
            #     bestSol = c33.deepcopy()

            # c44.cost = costFunction(c44.position)
            # if c44.cost < bestSol.cost:
            #     bestSol = c44.deepcopy()

            # Storing offsprings
            # popc.append(c1)
            # popc.append(c2)

            popc.append(c11)
            popc.append(c22)
            # popc.append(c33)
            # popc.append(c44)


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


def crossover(c1, c2):

    # a1 = c1.deepcopy()
    # a2 = c2.deepcopy()

    a3 = c1.deepcopy()
    a4 = c2.deepcopy()

    # partition = int(np.round(np.random.rand(1)*len(c1.position)-1))

    # for i in range(partition, len(c2.position)):
    #     a1.position[i] = c2.position[i]

    # for i in range(partition, len(c1.position)):
    #     a2.position[i] = c1.position[i]


    partition1 = -1
    while partition1 == -1:
        partition1 = int(np.round(np.random.rand(1)*len(c1.position)-1))

        if len(c1.position)%2 == 0:
            if partition1 == int(len(c1.position)/2)-1 or partition1 == int(len(c1.position)/2):
                partition1 = -1
        if partition1 == 0 or partition1 == len(c1.position)-1:
            partition1 = -1

    partition2 = len(c1.position) - partition1 -1

    if(partition1 > partition2):
        aa = partition1
        partition1 = partition2
        partition2 = aa

    for i in range(partition1, partition2):
        a3.position[i] = c2.position[i]

    for i in range(partition1, partition2):
        a4.position[i] = c1.position[i]

    return a3, a4


def mutation(x, mu):

    y = x.deepcopy()

    flag = np.random.rand(*x.position.shape) <= mu
    ind = np.argwhere(flag)

    y.position[ind] = 1 - y.position[ind]
    return y


def wheel_selection(p):

    s = np.sum(p)
    c = np.cumsum(p)
    flag = s*np.random.rand() <= c
    ind = np.argwhere(flag)
    return ind[0][0]