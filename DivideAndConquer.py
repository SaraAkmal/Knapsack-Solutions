
import time
import random

def DivideAndConquerKnapsack(Capacity, weights, values, numItems) -> int:
    # Base Case
    if numItems == 0 or Capacity == 0:
        return 0

    if (weights[numItems - 1] > Capacity):
        return DivideAndConquerKnapsack(Capacity, weights, values, numItems - 1)

    else:
        Solution_1 = DivideAndConquerKnapsack(Capacity, weights, values, numItems - 1)
        Solution_2 = DivideAndConquerKnapsack(Capacity - weights[numItems - 1], weights, values, numItems - 1)

        mySolution_1 = Solution_1
        mySolution_2 = Solution_2 + values[numItems - 1]

        if (mySolution_1 > mySolution_2):
            MaxSol = mySolution_1
        else:
            MaxSol = mySolution_2

    return MaxSol


def printValue(value):
    print("Value of items in the knapsack =", value)


Capacity = 300
numItems = 100
weights = {}
values = {}
i = 0
for i in range(numItems):
    weights[i] = random.randint(10, 50)
    values[i] = random.randint(10, 100)


valueWeightRatio = []

for index in range(numItems):
    valueWeightRatio.append(values[index] / weights[index])



print("\nRunning Divide  And Conquer Approach")
start_time = time.time()
DivideAndConquerValue = DivideAndConquerKnapsack(Capacity, weights, values, numItems)
printValue(DivideAndConquerValue)
end_time = time.time()
print('time needed: ', end_time - start_time)