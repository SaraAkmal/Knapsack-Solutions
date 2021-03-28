
import time
import random


def dynamicKnapsack(numItems, Capacity, values, weights):
    table = [[0 for x in range(Capacity + 1)] for x in range(numItems + 1)]

    for i in range(numItems + 1):

        for w in range(Capacity + 1):

            if i == 0 or w == 0:
                table[i][w] = 0

            elif weights[i - 1] <= w:
                table[i][w] = max(values[i - 1] + table[i - 1][w - weights[i - 1]], table[i - 1][w])

            else:
                table[i][w] = table[i - 1][w]

    return table[numItems][Capacity]

def printValue(value):
    print("Value of items in the knapsack =", value)


knapsackMaxCapacity = 300
numOfItems = 20
weightsOfItems = {}
valuesOfItems = {}
i = 0
for i in range(numOfItems):
    weightsOfItems[i] = random.randint(10, 100)
    valuesOfItems[i] = random.randint(10, 100)

print("\nDynamic programming Approach")
start_time = time.time()
maxValue = dynamicKnapsack(numOfItems, knapsackMaxCapacity, valuesOfItems, weightsOfItems)
printValue(maxValue)
end_time = time.time()
print('time needed: ', end_time - start_time)