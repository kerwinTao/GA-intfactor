import random

N = 85

pop = []

pop_size = 10
dna_size = 2


def fitness(dna):
    p = int(dna[0])
    q = int(dna[1])
    if p == 1 or q == 1:
        return 10000
    else:
        return abs(N - p * q)


def zeroes():
    dna = []
    p = ""
    q = ""

    for i in range(dna_size):
        p += '0'
        q += '0'

    dna.append(p)
    dna.append(q)

    return dna


def randomize():
    dna = []
    p = ""
    q = ""

    for i in range(dna_size):
        p += str(random.randint(0, 9))
        q += str(random.randint(0, 9))

    dna.append(p)
    dna.append(q)

    return dna


def crossover(p1, p2):
    child = zeroes()

    mid = int(random.randint(0, dna_size))
    for j in range(2):

        c = list(child[j])
        pa1 = list(p1[j])
        pa2 = list(p2[j])

        for i in range(dna_size):

            if i > mid:
                c[i] = pa1[i]
            else:
                c[i] = pa2[i]

        child[j] = "".join(c)
    return child


def mutate(dna, rate):
    for i in range(len(dna)):
        d = list(dna[i])
        for j in range(dna_size):
            if random.random() < rate:
                d[j] = str(random.randint(0, 9))
        dna[i] = "".join(d)
    dna.append(fitness(dna))
    return dna


def init_pop(pop):
    for i in range(pop_size):
        pop.append(randomize())
    for i in pop:
        i.append(fitness(i))


def select(pop):
    s = 0
    scores = []

    for i in pop:
        s += i[2]

    for i in pop:
        scores.append(i[2]/s)

    for i in pop:
        select = 0
        selector = random.random()
        while selector > 0:
            selector -= scores[select]
            select +=1
        select-=1
        return pop[select]



def ev(pop):
    fits = []
    for p in pop:
        fits.append(p[2])

    index = fits.index(min(fits))

    fittest = pop[index]

    p = int(fittest[0])
    q = int(fittest[1])
    n = p*q
    f = min(fits)

    print("Best Fitness = " + str(f) + " (p = " + str(p) + "; q = " + str(q) + ")")

    if n == N:
        print("Solution p = " + str(p) + "; q = " + str(q))
        return True


init_pop(pop)

stop = False
while not stop:
    stop = ev(pop)

    for k in range(len(pop)):

        pA = select(pop)
        pB = select(pop)
            
        ch = mutate(crossover(pA, pB), 0.08)

        pop[k] = ch

