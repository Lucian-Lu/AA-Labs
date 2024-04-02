import json
import random
import timeit
import matplotlib.pyplot as plt

# Shell sort
def shellSort(arr, n):
    gap = n // 2

    while gap > 0:
        j = gap
        while j < n:
            i = j - gap

            while i >= 0:
                if arr[i + gap] > arr[i]:
                    break
                else:
                    arr[i + gap], arr[i] = arr[i], arr[i + gap]

                i = i - gap
            j += 1
        gap = gap // 2
    return arr

# Quick sort
def partition(arr, l, h):
    i = (l - 1)
    x = arr[h]

    for j in range(l, h):
        if arr[j] <= x:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return (i + 1)


def quickSort(arr, l, h):
    size = h - l + 1
    stack = [0] * (size)

    top = -1

    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h

    while top >= 0:

        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        p = partition(arr, l, h)

        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1

        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h
    return arr

# Merge sort
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)
    return arr

# Heap sort
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        heapify(arr, i, 0)
    return arr

# Making an array with random elements (with max=size)
def make_array(size, arr=None) -> []:
    if arr is None:
        arr = []
    for i in range(size):
        arr.append(random.randint(0, size))
    return arr

# Writing the arrays to the json file
def write_to_json_file(file_path, data):
    with open(file_path, "w+") as json_file:
        json.dump(data, json_file, indent=4)


def plot_execution_times(iterations, execution_times_shell, execution_times_quick, execution_times_merge, execution_times_heap):

    # Plotting each algorithm's execution times
    plt.plot(iterations, execution_times_shell, label='Shell Sort')
    plt.plot(iterations, execution_times_quick, label='Quick Sort')
    plt.plot(iterations, execution_times_merge, label='Merge Sort')
    plt.plot(iterations, execution_times_heap, label='Heap Sort')

    plt.xlabel('Iteration')
    plt.ylabel('Execution Time (s)')
    plt.title('Execution Times of Sorting Algorithms')
    plt.legend()
    plt.show()


file_path = "./Array_to_sort.json"
size = 10000
count = 25
execution_times = []

for i in range(count):
    arr = []
    arr = make_array(size, arr)

    if i == count - 1:
        write_to_json_file(file_path, arr)

    sorting_algorithms = {
        "shell": (shellSort, (arr.copy(), size)),
        "quick": (quickSort, (arr.copy(), 0, size - 1)),
        "merge": (mergeSort, (arr.copy(), 0, size - 1)),
        "heap": (heapSort, (arr.copy(),))
    }
    for algorithm, (sorting_function, params) in sorting_algorithms.items():
        time_start = timeit.default_timer()

        sorting_function(*params)

        time_end = timeit.default_timer()
        execution_time = time_end - time_start
        execution_times.append(execution_time)

        if i == count - 1:
            file_path = f"./Array_sorted_{algorithm}.json"
            write_to_json_file(file_path, sorting_function(*params))


iterations = []
for i in range(1, count + 1):
    iterations.append(i)

execution_times_shell = execution_times[0::4]
execution_times_quick = execution_times[1::4]
execution_times_merge = execution_times[2::4]
execution_times_heap = execution_times[3::4]
plot_execution_times(iterations, execution_times_shell, execution_times_quick, execution_times_merge, execution_times_heap)
