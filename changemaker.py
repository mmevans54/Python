import json
import os
import sys
import time

def check_sorted(array):
    j = 0
    while j < (len(array) - 1):
        if array[j] > array[j + 1]:
            return False
        j += 1
    return True


def super_sort(test_set):
    not_sorted = True
    while not_sorted:

        index = 0
        while index < (len(test_set) - 1):
            # print(f"The test set is: {test_set}")
            if test_set[index + 1] < test_set[index]:
                test_set[index + 1], test_set[index] = test_set[index], test_set[index + 1]
            index += 1
        not_sorted = not check_sorted(test_set)
    return test_set


def get_highest_change_in_drawer(change_drawer, remaining_change_total):
    index = len(change_drawer) - 1
    while index >= 0:
        this_change = change_drawer[index]
        # print(f"this change: {this_change}")
        if this_change <= remaining_change_total:
            return this_change
        index -= 1
    return -1


def make_change_dynamic(change_drawer, remaining_change_total, change_count):

    if remaining_change_total > 0:
        next_change = -1

        # As long as we have a previously cached value, we look that up instead of recursing.
        if str(remaining_change_total) in cache_cache:
            while str(remaining_change_total) in cache_cache:
                # print("cache hit!")
                # print(f"The next change: {cache_cache[str(remaining_change_total)]}, the change_count: {change_count}")
                remaining_change_total -= cache_cache[str(remaining_change_total)]
                change_count += 1
                # print(f"The cache: {cash_cache}")
        else:
            next_change = get_highest_change_in_drawer(change_drawer, remaining_change_total)
            remaining_change_total -= next_change
            change_count += 1
            cash_cache[remaining_change_total] = next_change
        return make_change_dynamic(change_drawer, remaining_change_total, change_count)
    return change_count - 1


def make_change(change_drawer, remaining_change_total, change_count):
    if remaining_change_total > 0:
        next_change = get_highest_change_in_drawer(change_drawer, remaining_change_total)
        # print(f"The next change: {next_change}, the change_count: {change_count}")
        remaining_change_total -= next_change
        change_count += 1

        return make_change(change_drawer, remaining_change_total, change_count)
    return change_count - 1

# Here we have a cache to store information about our cache

def write_cache(the_cache):
    f = open("cache_file.txt", "w")
    f.write(json.dumps(cash_cache))
    f.close()

def load_cache():
    return json.load(open("cache_file.txt"))

cash_cache = {}

if __name__ == '__main__':
    # print(f"The result of the sort is: {super_sort([5, 7, 19, 1, 0, 5])}")
    # print(f"The highest change in the drawer is: {get_highest_change_in_drawer([0, 1, 5, 5, 7, 19, 25, 30], 20)}")
    remaining_change_total = int(sys.argv[1])
    change_drawer = []
    for arg in sys.argv[2:]:
        change_drawer.append(int(arg))

    print("running software")
    # Sort the cache drawer, to make it easy to pick the largest item (plus I made one in previous assingment that is pretty fast)
    change_drawer = super_sort(change_drawer)

    # Ensure there is atleast 1, 1 in the drawer
    if not 1 in change_drawer:
        change_drawer.insert(0, 1)

    print(f"the change drawer: {change_drawer}")
    print(f"The remaining total: {remaining_change_total}")


    # start_time = time.time()
    # print(f"The change is: {make_change(change_drawer, remaining_change_total, 1)}")
    # print(f"Run time for make change (recursive/static): {time.time() - start_time}" )

    cache_cache = load_cache()
    start_time = time.time()
    print(f"The dynamic change is: {make_change_dynamic(change_drawer, remaining_change_total, 1)}")
    print(f"Run time for make change (recursive/dynamic): {time.time() - start_time}")

    write_cache(cache_cache)
