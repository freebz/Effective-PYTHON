def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # ...

    return wrapper

@trace
def fibonacci(n):
    # ...



help(fibonacci)

>>>
Help on function fibonacci in module __main__:

fibonacci(n)
    Return the n-th Fibonacci number
