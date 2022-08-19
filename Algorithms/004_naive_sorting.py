def naive_sort(num_list):
    for scanIndex in range(0, len(num_list)):
        minIndex = scanIndex

        for compIndex in range(scanIndex + 1, len(num_list)):
            if num_list[compIndex] < num_list[minIndex]:
                minIndex = compIndex

        if minIndex != scanIndex:
            num_list[scanIndex], num_list[minIndex] = num_list[minIndex], num_list[scanIndex]
            print(num_list)


# ============== #
# The main code  #
# ============== #
# This code naively sort a list of numbers.

# E.G.
import random

data = random.sample(range(0, 100), 10)
print(data)
naive_sort(data)
