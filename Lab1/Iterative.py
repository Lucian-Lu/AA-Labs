def iterative_fibonacci(nr):
    if nr == 0:
        return cache[0]
    elif nr == 1:
        return cache[1]
    else:
        for i in range(1, nr):
            cache.append(cache[i] + cache[i - 1])
        return cache[nr]


cache = [0, 1]
print(iterative_fibonacci(100000))
