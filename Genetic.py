from numpy.random import randint
from random import randint as RandomInt
from random import choice
from itertools import chain
import random
import time


def printValue(value):
    print("Value of items in the knapsack =", value)

def test(Num_offsprings) -> int:

    weights = {}
    values = {}
    Capacity = 50
    objects_Info = []
#Random generation of knapsack
    numItems = 5
    i = 0
    for i in range(numItems):
        weights[i] = random.randint(10, 30)
        values[i] = random.randint(10, 100)
        objects_Info.append([weights[i], values[i]])

##########
    # Capacity = 16
    # numItems = 4
    # weights= [2,5,10,5]
    # values = [20,30,50,10]
    # i = 0
    # for i in range(numItems):
    #     objects_Info.append([weights[i], values[i]])
###########


    Offspring = randint(2, size=(Num_offsprings, numItems))
    Fitness = []
    start_time = time.time()
    for i in range(Num_offsprings):
        WeightSum = 0
        ValueSum = 0
        for j in range(numItems):
            WeightSum = WeightSum + (Offspring[i][j] * objects_Info[j][0])
        for j in range(numItems):
            if (WeightSum <= Capacity):
                ValueSum = ValueSum + Offspring[i][j] * objects_Info[j][1]
            else:
                ValueSum = 0
        Fitness.append(ValueSum)

    SelectionItems = []
    SelectionFitness = []
    for i in range(len(Fitness)):
        if (Fitness[i] >= (Capacity / 10)):
            SelectionItems.append(list(Offspring[i]))
    SelectionItems1 = []
    end = True
    counter = 0

    while (end):
        for i in range(int(Num_offsprings)):
            if not SelectionItems:
                print("Empty Selection")
                return 0
            else:
                S1 = choice(SelectionItems)
                S2 = choice(SelectionItems)
                CrossOverPoint = RandomInt(1, numItems)
                NextGen = list(chain(S1[0:CrossOverPoint], S2[CrossOverPoint:]))
                SelectionItems1.append(NextGen)


        Fitness = []
        for i in range(Num_offsprings):
            WeightSum = 0
            ValueSum = 0
            for j in range(numItems):
                WeightSum = WeightSum + (SelectionItems1[i][j] * objects_Info[j][0])
            for j in range(numItems):
                if (WeightSum <= Capacity):
                    ValueSum = ValueSum + SelectionItems1[i][j] * objects_Info[j][1]
                else:
                    ValueSum = 0
        Fitness.append(ValueSum)

        if (counter == 1000):
            fitesst = max(Fitness)
            print("\nGenetic Approach")
            printValue(fitesst)
            a = Fitness.index(fitesst)
            print(SelectionItems1[a])
            end_time = time.time()
            print('time needed: ', end_time - start_time)
            exit()

        SelectionItems = []
        for i in range(len(Fitness)):
            if (Fitness[i] >= (Capacity / 2)):
                SelectionItems.append(list(SelectionItems1[i]))
        SelectionItems1 = []
        counter += 1


    return 0


test(100)




