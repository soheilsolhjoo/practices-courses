import random


def search(search_list, key):
    mid = int(len(search_list) / 2)

    if mid == 0:
        print("Key Not Found!")
        return key
    elif key == search_list[mid]:
        print("Key Found!")
        return search_list[mid]
    elif key > search_list[mid]:
        search(search_list[mid:len(search_list)], key)
    else:
        search(search_list[0:mid], key)


# ============== #
# The main code  #
# ============== #
# This code looks for a key within a search list.
# The code requires a sorted list. I'll write a sorting function later. For now, I use "sorted" function of python.

list_size = 50
search_list = random.sample(range(0, 100), list_size)
n = int(input("Enter a key (an integer) to be searched within the randomly generated list: "))
search(sorted(search_list), n)
