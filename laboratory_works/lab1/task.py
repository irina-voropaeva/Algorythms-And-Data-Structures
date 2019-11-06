import random
import sys
import time

sys.setrecursionlimit(10000)


# Generating random list
def generate_rand_list(size):
    return [random.randint(0, 1000) for i in range(0, size)]


# Function-decorator for other functions. Returns decorated function execution time
def how_long(f):
    def tmp(*args, **kwargs):
        t = time.time()
        f(*args, **kwargs)
        need_time = time.time() - t
        return need_time

    return tmp


# Bubble sort
@how_long
def sort_bubble(data):
    for i in range(len(data)):
        for j in range(len(data) - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


# Insertion sort
@how_long
def insertion_sort(A):
    for i in range(1, len(A)):
        # В new_elem сохранили значение A[i]
        new_elem = A[i]
        # Начиная с элемента A[i - 1]
        j = i - 1
        # все элементы, которые больше new_elem
        while j >= 0 and A[j] > new_elem:
            # сдвигаем вправо на 1
            A[j + 1] = A[j]
            j -= 1
        # На свободное место записываем new_elem
        A[j + 1] = new_elem


@how_long
def quick_sort(data):
    return sort_quick_helper(data)


def sort_quick_helper(data):
    if not data:
        return data

    less = []
    equal = []
    bigger = []
    pivot = data[0]
    for i in data:
        if i > pivot:
            bigger.append(i)
        elif i < pivot:
            less.append(i)
        else:
            equal.append(i)
    return sort_quick_helper(less) + equal + sort_quick_helper(bigger)
