def factorial_loop(n):
    if n == 0:
        return 1   # indentation is very key in loops
    else:
        return n * factorial_loop(n - 1)
print(factorial_loop(4))