# Author: Morgan Orahood
# Date: 2/24/2021
# Description: This program will find the amount of time is takes to sort through different sizes of data using bubble
# sort and insertion sort. It will then produce a graph that represents the data.

import random
import time
from matplotlib import pyplot
from functools import wraps


def sort_timer(func):
    """Times how many seconds it takes the decorated function to run"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        """A wrapper function that returns the current time"""
        func(*args, **kwargs)
        start = time.perf_counter()
        end = time.perf_counter()
        current_time = end - start
        print(current_time)
        return current_time
    return wrapper


@sort_timer
def bubble_sort(a_list):
    """Sorts a_list in ascending order"""
    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp


@sort_timer
def insertion_sort(a_list):
    """Sorts a_list in ascending order"""
    for index in range(1, len(a_list)):
        value = a_list[index]
        pos = index - 1
        while pos >= 0 and a_list[pos] > value:
            a_list[pos + 1] = a_list[pos]
            pos -= 1
        a_list[pos + 1] = value


def compare_sorts(bubble_sort, insertion_sort):
    """Randomly generate a list of numbers that are 10 different sizes. After bubble sort and insertion sort have
    sorted through each list, the current times are added to empty lists. The times are then plotted on a graphs y-axis
    along with the different list sizes referred by the x-axis."""
    diff_list_sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    # List for random numbers
    my_list = []
    # List of bubble sort times (to be plotted)
    bubble_sort_times = []
    # List of insertion sort times (to be plotted)
    insertion_sort_times = []
    # Iterates through each list size and adds random numbers to my_list
    for sizes in diff_list_sizes:
        for i in range(1, sizes + 1):
            random_nums = random.randint(1, 10000)
            my_list.append(random_nums)
        copy_of_list = list(my_list)
        print(sizes)
        # Add to empty lists
        bubble_sort_times.append(bubble_sort(my_list))
        insertion_sort_times.append(insertion_sort(copy_of_list))
    # Calls to create graph
    pyplot.plot(diff_list_sizes, bubble_sort_times, 'ro--', linewidth=2)
    pyplot.plot(diff_list_sizes, insertion_sort_times, 'go--', linewidth=2)
    pyplot.xlabel("The number of elements being sorted")
    pyplot.ylabel("The time in seconds")
    pyplot.show()

compare_sorts(bubble_sort, insertion_sort)