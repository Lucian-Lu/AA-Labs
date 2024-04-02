from math import *


def fibonacci_binet(nr):
    sqrt_5 = sqrt(5)
    golden_ratio = (1 + sqrt_5) / 2

    fib_n = (golden_ratio**nr - (-1 / golden_ratio)**nr) / sqrt_5
    return round(fib_n)


result_binet = fibonacci_binet(100)
print(result_binet)
