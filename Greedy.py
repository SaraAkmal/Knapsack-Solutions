import random
import time

def greedyKnapsack(Capacity, values, weights, Ratio):

    knapsack = []
    Weight = 0
    Value = 0

    while (Weight <= Capacity):

        maxItem = max(Ratio)

        indexOfMaxItem = Ratio.index(maxItem)

        if weights[indexOfMaxItem] + Weight <= Capacity:
            knapsack.append(indexOfMaxItem + 1)
            Weight += weights[indexOfMaxItem]
            Value += values[indexOfMaxItem]
            Ratio[indexOfMaxItem] = -1
        else:
            break
    return Value

def printValue(value):
    print("Value of items in the knapsack =", value)


Capacity = 300
numOfItems = 1000
weights = {}
values = {}
i = 0
for i in range(numOfItems):
    weights[i] = random.randint(10, 100)
    values[i] = random.randint(10, 100)


Ratio = []

for index in range(numOfItems):
    Ratio.append(values[index] / weights[index])


print("\nGreedy Approach")
start_time = time.time()
maxValue = greedyKnapsack(Capacity, values, weights, Ratio)
printValue(maxValue)
end_time = time.time()
print('time needed: ', end_time - start_time)