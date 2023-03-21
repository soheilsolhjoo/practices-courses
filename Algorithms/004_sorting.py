def fun_timer(fun, n):
    """Measure the running time of "fun" with an input argument n."""
    tic = timeit.default_timer()
    returned = fun(n)
    toc = timeit.default_timer()
    return returned, toc - tic


"""PART 1: Brute force algorithms"""


def naive_sort(num_list):
    steps = 0
    # Select numbers one-by-one, from index 0.
    for scanIndex in range(0, len(num_list)):
        minIndex = scanIndex

        # Compare the selected number with the rest, till a smaller one is found.
        for compIndex in range(scanIndex + 1, len(num_list)):
            if num_list[compIndex] < num_list[minIndex]:
                minIndex = compIndex
                steps += 1

        # If a smaller number is found, switch positions of the two numbers.
        if minIndex != scanIndex:
            num_list[scanIndex], num_list[minIndex] = num_list[minIndex], num_list[scanIndex]
            # print(num_list)
            steps += 1
    return num_list, steps


def insertion_sort(num_list):
    steps = 0
    # Select numbers one-by-one, from index 1.
    for scanIndex in range(1, len(num_list)):
        temp = num_list[scanIndex]
        minIndex = scanIndex

        # Compare the selected number with numbers in left, and
        # sort them one-by-one, until the moved number is larger than the compared one.
        while minIndex > 0 and temp < num_list[minIndex - 1]:
            num_list[minIndex] = num_list[minIndex - 1]
            minIndex -= 1
            steps += 1
        num_list[minIndex] = temp
        # print(num_list)

    return num_list, steps


"""PART 2: Merge Sort algorithm"""


def mergeSort(num_list, div_steps=0, steps=0):
    """ MERGE-SORT method contains two functions: mergeSort() & merge()"""
    # The function "mergeSort()" divide the list into smaller pieces, and assign them to LEFT and RIGHT.
    # This continues until the length of each side becomes 0 of 1.

    # Determine whether the list is broken into individual pieces.
    if len(num_list) < 2:
        return num_list, div_steps

    # Find the middle of the list.
    middle = len(num_list) // 2

    # Break the list into two pieces.
    # div_steps counts how many times the list gets divided in two segments
    div_steps += 1
    left = mergeSort(num_list[:middle], div_steps, steps)
    div_steps = left[1] + 1
    right = mergeSort(num_list[middle:], div_steps, steps)

    div_steps = right[1]

    # Merge the two sorted pieces into a larger piece.
    # steps count the how many times the comparison and sorting function gets called
    merged = merge(left[0], right[0])
    num_list = merged[0]
    steps += merged[1]
    return num_list, div_steps, steps


def merge(left, right):
    steps = 0
    """ MERGE-SORT method contains two functions: mergeSort() & merge()"""
    # This function performs the merging of thw two sides, and sort their elements.

    # When the left side or the right side is empty, it means that this is an individual item and is already sorted.
    if not len(left):
        return left, steps
    if not len(right):
        return right, steps

    # Define variables used to merge the two pieces.
    merged_list = []
    leftIndex = 0
    rightIndex = 0
    totalLen = len(left) + len(right)

    # Keep working until all of the items are merged.
    while len(merged_list) < totalLen:
        # Perform the required comparisons and merge the pieces according to value.
        if left[leftIndex] < right[rightIndex]:
            merged_list.append(left[leftIndex])
            leftIndex += 1
        else:
            merged_list.append(right[rightIndex])
            rightIndex += 1

        steps += 1
        # When the left side or the right side is longer, add the remaining elements to the merged_list.
        if leftIndex == len(left) or rightIndex == len(right):
            merged_list.extend(left[leftIndex:] or right[rightIndex:])
            break
    return merged_list, steps


# ============== #
# The main code  #
# ============== #
# This code naively sort a list of numbers.

# E.G.
import random, timeit

data = random.sample(range(0, 100), 10)
sort_naive = fun_timer(naive_sort, data.copy())
sort_insertion = fun_timer(insertion_sort, data.copy())
sort_mergeSort = fun_timer(mergeSort, data.copy())

sorted_list = sort_naive[0][0]

print(
    "The following is the randomly generated list of numbers and its sorted version:\n{}\n{}".format(data, sorted_list))
print("Sorted by the NAIVE method in {} steps, \t\t sec elapsed {}".format(sort_naive[0][1], sort_naive[1]))
print("Sorted by the INSERTION method in {} steps, \t sec elapsed {}".format(sort_insertion[0][1], sort_insertion[1]))
print("Sorted by the SORT-MERGE method in {} (for dividing) and {} (for comparison) steps, \t sec elapsed {}".
      format(sort_mergeSort[0][1], sort_mergeSort[0][2], sort_mergeSort[1]))
