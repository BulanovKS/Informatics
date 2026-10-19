import numpy as np
import matplotlib.pyplot as plt
import random
import time

def array_generator(nums):
    S = len(nums)
    nums = [random.randint(0, 1000000) for _ in range(S)]

def is_sorted(nums):
    S = len(nums)
    for i in range(S - 1):
        if nums[i + 1] > nums[i]:
            return False
    return True

def bubble_sort(nums):  
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

def insertion_sort(nums):  
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert

def test_sort_from_2_param(func, test_array, N, K):
    result_time = 0

    for k in range(N):
        array_generator(test_array)
            
        t1 = time.time()
        func(test_array)
        t2 = time.time()

        result_time += t2 - t1
    return result_time / K

file = open("python_sorts.csv", "w", encoding="utf_8")

test_array = [0 for i in range(100000)]
test_size = [10, 100, 500, 1000, 5000, 10000, 25000, 50000, 75000, 100000]
number_of_iterations = [10, 10, 10, 5, 5, 5, 3, 3, 3, 2]

file.write("Type of array,Number,Time of bubble_sort,Time of insertion_sort\n")

flag = 0
for j in range(10):
    N = test_size[j]
    K = number_of_iterations[j]

    bubble_time = test_sort_from_2_param(bubble_sort, test_array, N, K)
    print(str(N) + ": Time buble_sort " + str(bubble_time))
    insertion_time = test_sort_from_2_param(insertion_sort, test_array, N, K)
    print(str(N) + ": Time insertion_sort " + str(insertion_time))

    file.write(str(flag) + "," + str(N) + "," + str(bubble_time) + "," + str(insertion_time))