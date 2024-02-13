def fibonacci_pisano_period(n, m):
    if n == 0:
        return 0

    period = [0, 1]
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, (a + b) % m
        period.append(b)
        if period[-2:] == [0, 1]:
            period.pop()
            break

    index = n % len(period)
    return period[index]


# Pisano Peroid approach
result_pisano_period = fibonacci_pisano_period(10, 1000)
print(result_pisano_period)