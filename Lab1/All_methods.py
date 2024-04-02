import timeit
import matplotlib.pyplot as plt
import numpy as np
import sys
from decimal import Decimal, getcontext
from math import sqrt

sys.setrecursionlimit(3000)
getcontext().prec = 1000
MOD = 1000000007
res = [0] * 2


def recursive_fibonacci(nr):
    if nr == 0:
        return 0
    elif nr == 1:
        return 1
    else:
        return recursive_fibonacci(nr - 1) + recursive_fibonacci(nr - 2)


def calculate_execution_times(n):
    execution_times = np.zeros(n+1, dtype=float)
    terms_to_print = np.unique(np.linspace(5, n, 17, dtype=int))

    for term in range(n+1):
        start_time = timeit.default_timer()
        result = recursive_fibonacci(term)
        end_time = timeit.default_timer()
        execution_time = (end_time - start_time) * 1000
        execution_times[term] = execution_time

        if term in terms_to_print:
            print(f"Fibonacci({term}), Execution Time: {execution_time} milliseconds")

    plt.plot(range(n+1), execution_times, marker='o')
    plt.title('Execution Time for Recursive Method')
    plt.xlabel('Term')
    plt.ylabel('Execution Time (milliseconds)')
    plt.show()


def dynamic_fibonacci(nr, cache=None):
    if cache is None:
        cache = {}
    if nr == 0:
        return 0
    elif nr == 1:
        return 1
    else:
        if cache.get(nr - 1) is None:
            cache[nr - 1] = dynamic_fibonacci(nr - 1, cache)
        if cache.get(nr - 2) is None:
            cache[nr - 2] = dynamic_fibonacci(nr - 2, cache)
        return cache[nr - 1] + cache[nr - 2]

def calculate_execution_times_dynamic(n):
    execution_times = []
    terms_to_print = np.unique(np.linspace(5, n, 17, dtype=int))

    for term in terms_to_print:
        start_time = timeit.default_timer()
        dynamic_fibonacci(term)
        end_time = timeit.default_timer()
        execution_time = (end_time - start_time) * 1000
        execution_times.append(execution_time)

        print(f"Fibonacci({term}), Execution Time: {execution_time} milliseconds")

    plt.plot(terms_to_print, execution_times, marker='o')
    plt.title('Dynamic Fibonacci Execution Time')
    plt.xlabel('Term')
    plt.ylabel('Execution Time (milliseconds)')
    plt.show()


def iterative_fibonacci(nr, cache=None):
    if cache == None:
        cache = [0, 1]
    if nr == 0:
        return cache[0]
    elif nr == 1:
        return cache[1]
    else:
        for i in range(1, nr):
            cache.append(cache[i] + cache[i - 1])
        return cache[nr]

def calculate_execution_times_iterative(n):
    execution_times = []
    terms_to_print = np.unique(np.linspace(5, n, 17, dtype=int))

    for term in terms_to_print:
        start_time = timeit.default_timer()
        iterative_fibonacci(term)
        end_time = timeit.default_timer()
        execution_time = (end_time - start_time) * 1000
        execution_times.append(execution_time)

        print(f"Fibonacci({term}), Execution Time: {execution_time} milliseconds")

    plt.plot(terms_to_print, execution_times, marker='o')
    plt.title('Iterative Fibonacci Execution Time')
    plt.xlabel('Term')
    plt.ylabel('Execution Time (milliseconds)')
    plt.show()


def fibonacci_binet(nr):
    sqrt_5 = Decimal(sqrt(5))
    golden_ratio = (1 + sqrt_5) / 2

    fib_n = (golden_ratio**nr - (-1 / golden_ratio)**nr) / sqrt_5
    return round(fib_n)

def calculate_execution_times_binet(n):
    execution_times = []
    errors = []
    terms_to_print = np.unique(np.linspace(5, n, 17, dtype=int))

    for term in terms_to_print:
        start_time = timeit.default_timer()
        result = fibonacci_binet(term)
        end_time = timeit.default_timer()
        execution_time = (end_time - start_time) * 1000
        execution_times.append(execution_time)
        true_result = iterative_fibonacci(term)
        error = abs(result - true_result)
        errors.append(error)
        # , Error: {error}
        print(f"Fibonacci({term}), Execution Time: {execution_time} milliseconds")
    # print(errors)
    plt.plot(terms_to_print, execution_times, marker='o')
    plt.title('Binet Formula Fibonacci Execution Time')
    plt.xlabel('Term')
    plt.ylabel('Execution Time (milliseconds)')
    plt.show()

    plt.plot(terms_to_print, errors, marker='o')
    plt.title('Binet Formula Errors')
    plt.xlabel('Term')
    plt.ylabel('Error')
    plt.show()


def multiply(a, b):
    mul = [[0 for x in range(3)] for y in range(3)]
    for i in range(3):
        for j in range(3):
            mul[i][j] = 0
            for k in range(3):
                mul[i][j] += a[i][k] * b[k][j]

    for i in range(3):
        for j in range(3):
            a[i][j] = mul[i][j]
    return a

def power(F, n):
    M = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
    if n == 1:
        return F[0][0] + F[0][1]
    power(F, n // 2)
    F = multiply(F, F)
    if n % 2 != 0:
        F = multiply(F, M)
    return F[0][0] + F[0][1]


def findNthTerm(n):
    F = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
    return power(F, n - 2)


def calculate_execution_times_matrix_power(n):
    execution_times = []
    terms_to_print = np.unique(np.linspace(5, n, 17, dtype=int))

    for term in terms_to_print:
        start_time = timeit.default_timer()
        result = findNthTerm(term)
        end_time = timeit.default_timer()
        execution_time = (end_time - start_time) * 1000
        execution_times.append(execution_time)

        print(f"Fibonacci({term}), Execution Time: {execution_time} milliseconds")

    plt.plot(terms_to_print, execution_times, marker='o')
    plt.title('Matrix Power Fibonacci Execution Time')
    plt.xlabel('Term')
    plt.ylabel('Execution Time (milliseconds)')
    plt.show()


def FastDoubling(n, res):
    if n == 0:
        res[0] = 0
        res[1] = 1
        return

    FastDoubling(n // 2, res)
    a = res[0]
    b = res[1]
    c = 2 * b - a
    if c < 0:
        c += MOD
    c = (a * c) % MOD
    d = (a * a + b * b) % MOD
    if n % 2 == 0:
        res[0] = c
        res[1] = d
    else:
        res[0] = d
        res[1] = c + d

def calculate_execution_times_fast_doubling(n):
    execution_times = []
    terms_to_print = np.unique(np.linspace(5, n, 17, dtype=int))

    for term in terms_to_print:
        start_time = timeit.default_timer()
        FastDoubling(term, res)
        end_time = timeit.default_timer()
        execution_time = (end_time - start_time) * 1000
        execution_times.append(execution_time)

        print(f"Fibonacci({term}), Execution Time: {execution_time} milliseconds")

    plt.plot(terms_to_print, execution_times, marker='o')
    plt.title('Fast Doubling Fibonacci Execution Time')
    plt.xlabel('Term')
    plt.ylabel('Execution Time (milliseconds)')
    plt.show()


# Method #1
# n = 40
# calculate_execution_times(n)

# Method #2
# n = 2000
# calculate_execution_times_dynamic(n)

# Method #3
# n = 2000
# calculate_execution_times_iterative(n)

# Method #4
# n = 10000
# calculate_execution_times_binet(n)

# Method #5
# n = 10000
# calculate_execution_times_matrix_power(n)

# Method #6
# n = 10000
# calculate_execution_times_fast_doubling(n)

