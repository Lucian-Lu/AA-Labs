import timeit
import matplotlib.pyplot as plt
import numpy as np
from decimal import Decimal, getcontext
from math import sqrt

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

def calculate_execution_times_recursive(n, color):
    execution_times = np.zeros(n + 1, dtype=float)

    for term in range(n + 1):
        start_time = timeit.default_timer()
        recursive_fibonacci(term)
        end_time = timeit.default_timer()
        execution_time = (end_time - start_time) * 1000
        execution_times[term] = execution_time

    plt.plot(range(n + 1), execution_times, marker='o', label=f'Recursive ({color})')

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

def calculate_execution_times_dynamic(n, color):
    execution_times = []
    terms_to_print = np.unique(np.linspace(5, n, 17, dtype=int))

    for term in terms_to_print:
        start_time = timeit.default_timer()
        dynamic_fibonacci(term)
        end_time = timeit.default_timer()
        execution_time = (end_time - start_time) * 1000
        execution_times.append(execution_time)

    plt.plot(terms_to_print, execution_times, marker='o', label=f'Dynamic ({color})')

def iterative_fibonacci(nr, cache=None):
    if cache is None:
        cache = [0, 1]
    if nr == 0:
        return cache[0]
    elif nr == 1:
        return cache[1]
    else:
        for i in range(1, nr):
            cache.append(cache[i] + cache[i - 1])
        return cache[nr]

def calculate_execution_times_iterative(n, color):
    execution_times = []
    terms_to_print = np.unique(np.linspace(5, n, 17, dtype=int))

    for term in terms_to_print:
        start_time = timeit.default_timer()
        iterative_fibonacci(term)
        end_time = timeit.default_timer()
        execution_time = (end_time - start_time) * 1000
        execution_times.append(execution_time)

    plt.plot(terms_to_print, execution_times, marker='o', label=f'Iterative ({color})')

def fibonacci_binet(nr):
    sqrt_5 = Decimal(sqrt(5))
    golden_ratio = (1 + sqrt_5) / 2

    fib_n = (golden_ratio**nr - (-1 / golden_ratio)**nr) / sqrt_5
    return round(fib_n)

def calculate_execution_times_binet(n, color):
    execution_times = []
    terms_to_print = np.unique(np.linspace(5, n, 17, dtype=int))

    for term in terms_to_print:
        start_time = timeit.default_timer()
        fibonacci_binet(term)
        end_time = timeit.default_timer()
        execution_time = (end_time - start_time) * 1000
        execution_times.append(execution_time)

    plt.plot(terms_to_print, execution_times, marker='o', label=f'Binet Formula ({color})')

def power(F, n):
    M = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
    if n == 1:
        return F[0][0] + F[0][1]
    power(F, n // 2)
    F = multiply(F, F)
    if n % 2 != 0:
        F = multiply(F, M)
    return F[0][0] + F[0][1]


def multiply(a, b):
    mul = [[0 for x in range(3)]
           for y in range(3)]
    for i in range(3):
        for j in range(3):
            mul[i][j] = 0
            for k in range(3):
                mul[i][j] += a[i][k] * b[k][j]

    for i in range(3):
        for j in range(3):
            a[i][j] = mul[i][j]
    return a


def findNthTerm(n):
    F = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
    return power(F, n - 2)

def calculate_execution_times_matrix_power(n, color):
    execution_times = []
    terms_to_print = np.unique(np.linspace(5, n, 17, dtype=int))

    for term in terms_to_print:
        start_time = timeit.default_timer()
        findNthTerm(term)
        end_time = timeit.default_timer()
        execution_time = (end_time - start_time) * 1000
        execution_times.append(execution_time)

    plt.plot(terms_to_print, execution_times, marker='o', label=f'Matrix Power ({color})')

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

def calculate_execution_times_fast_doubling(n, color):
    execution_times = []
    terms_to_print = np.unique(np.linspace(5, n, 17, dtype=int))

    for term in terms_to_print:
        start_time = timeit.default_timer()
        FastDoubling(term, res)
        end_time = timeit.default_timer()
        execution_time = (end_time - start_time) * 1000
        execution_times.append(execution_time)

    plt.plot(terms_to_print, execution_times, marker='o', label=f'Fast Doubling ({color})')

if __name__ == "__main__":
    n = 30

    calculate_execution_times_recursive(n, 'blue')
    calculate_execution_times_dynamic(n, 'orange')
    calculate_execution_times_iterative(n, 'green')
    calculate_execution_times_binet(n, 'red')
    calculate_execution_times_matrix_power(n, 'purple')
    calculate_execution_times_fast_doubling(n, 'brown')

    plt.title('Execution Time for Fibonacci Methods')
    plt.xlabel('Term')
    plt.ylabel('Execution Time (milliseconds)')
    plt.legend()
    plt.show()
