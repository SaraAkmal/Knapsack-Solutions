import random
import time

def Backtrack(weights, values, length, maxValue):

    if maxValue == 0 or length == 0:
        return 0

    if len(weights) != len(values):
        return 0

    if weights[length - 1] > maxValue:

        return Backtrack(weights, values, length - 1, maxValue)
    else:

        return max(values[length - 1] + Backtrack(weights, values, length - 1, maxValue - weights[length - 1]),
                   Backtrack(weights, values, length - 1,
                             maxValue))


def printValue(value):
    print("Value of items in the knapsack =", value)


capacity = 300
numOfItems = 10
weights = {}
values = {}
i = 0
for i in range(numOfItems):
    weights[i] = random.randint(10, 100)
    values[i] = random.randint(10, 100)



start_time = time.time()
maxValue = Backtrack(weights, values, len(values), capacity)
print("Approach BackTrack")
printValue(maxValue)
end_time = time.time()
print('time needed: ', end_time - start_time)

