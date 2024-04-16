def dynamic_fibonacci(nr):
    if nr == 0:
        return 0
    elif nr == 1:
        return 1
    else:
        if cache.get(nr - 1) is None:
            cache[nr - 1] = dynamic_fibonacci(nr - 1)
        if cache.get(nr - 2) is None:
            cache[nr - 2] = dynamic_fibonacci(nr - 2)
        return cache[nr - 1] + cache[nr - 2]

# Dynamic programming approach
cache = {}
print(dynamic_fibonacci(100))
