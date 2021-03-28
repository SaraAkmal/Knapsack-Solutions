import random
import time

def Sort(weights, values):
    def ratio(e):
        return e[1] / e[0]

    v = range(len(values))
    X = [[weights[x], values[x]] for x in v]
    Y = sorted(X, key=ratio)
    S = [Y[x][0] for x in v]
    U = [Y[x][1] for x in v]
    return S, U


def optimistic(values, weights, p):
    Sum = weights[2]
    j = weights[0]
    while j > weights[1][p - 1] and p > 0:
        a = values[p - 1]
        Sum += a
        j -= weights[1][p - 1]
        p -= 1
    if p != 0:
        a = values[p - 1]
        b = weights[1][p - 1]
        Sum += int(a * (j / b))
    return Sum


def fourth(e):
    return e[0][3]


def third(e):
    return e[2]


def resolve(n, values, weights, p, r=[], Q=[]):
    if p == 0:
        return weights, r
    z = weights.copy()
    z[0] -= weights[1][p - 1]
    z[2] += values[p - 1]
    z[3] = optimistic(values, weights, p)
    weights[3] = optimistic(values, weights, p - 1)
    if z[0] >= 0:
        Q += [[weights, p - 1, r], [z, p - 1, r + [p]]]
    else:
        Q += [[weights, p - 1, r]]
    Q = sorted(Q, key=fourth, reverse=True)
    best = Q.pop(0)
    return resolve(n, values, best[0], best[1], best[2], Q)


def control(n, weights, values):
    X = Sort(weights, values)
    weights = X[0]
    values = X[1]
    T = [n, weights, 0, 0]
    return resolve(n, values, T, len(weights))


def test_it():

    n = 3000
    weights = {}
    values = {}
    i = 0
    for i in range(50):
        weights[i] = random.randint(10, 100)
        values[i] = random.randint(10, 100)

    print_it(n, weights, values)


def print_it(n, weights, values):
    start_time = time.time()
    res = control(n, weights, values)
    end_time = time.time()
    print('Maximum value = ' + str(res[0][2]))
    print('time needed: ', end_time - start_time)
    return n, Sort(weights, values)



x = test_it()
