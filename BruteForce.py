import time
import random

def bruteKnapsack(Capacity, weights, values, numItems) -> int:
    # Base Case
    if numItems == 0 or Capacity == 0:
        return 0
    if (weights[numItems - 1] > Capacity):
        return bruteKnapsack(Capacity, weights, values, numItems - 1)
    else:
        value = max(values[numItems - 1] + bruteKnapsack(Capacity - weights[numItems - 1], weights, values, numItems - 1),
                    bruteKnapsack(Capacity, weights, values, numItems - 1))
    return value

def printValue(value):
    print("Value of items in the knapsack =", value)


Capacity = 300
numItems = 10
Weights = {}
Values = {}
i = 0
for i in range(numItems):
    Weights[i] = random.randint(10, 100)
    Values[i] = random.randint(10, 100)


valueWeightRatio = []

for index in range(numItems):
    valueWeightRatio.append(Values[index] / Weights[index])



start_time = time.time()
print("\nBrute Force Approach")
maxValue = bruteKnapsack(Capacity, Weights, Values, numItems)
printValue(maxValue)
end_time = time.time()
print('time needed: ', end_time - start_time)
