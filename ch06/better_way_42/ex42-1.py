def trace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('%s(%r, %r) -> %r' %
              (func.__name__, args, kwargs, result))
        return result
    return wrapper


@trace
def fibonacci(n):
    """n번째 피보나치 수를 반환한다."""
    if n in (0, 1):
        return n
    return (fibonacci(n - 2) + fibonacci(n - 1))


fibonacci = trace(fibonacci)


fibonacci(3)

>>>
fibonacci((1,), {}) -> 1
fibonacci((0,), {}) -> 0
fibonacci((1,), {}) -> 1
fibonacci((2,), {}) -> 1
fibonacci((3,), {}) -> 2


print(fibonacci)

>>>
<function trace.<locals>.wrapper at 0xb70e241c>


help(fibonacci)

>>>
Help on function wrapper in module __main__:

wrapper(*args, **kwargs)
