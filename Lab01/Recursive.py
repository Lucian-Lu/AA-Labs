def recursive_fibonacci(nr):
    if nr == 0:
        return 0
    elif nr == 1:
        return 1
    else:
        return recursive_fibonacci(nr - 1) + recursive_fibonacci(nr - 2)

# Recursive approach
print(recursive_fibonacci(10))
