def safe_division_c(number, divisor, *,
                    ignore_overflow=False,
                    ignore_zero_division=False):
    # ...


safe_division_c(1, 10**500, True, False)

>>>
TypeError: safe_division_c() takes 2 positional arguemnts but 4 were given


safe_division_c(1, 0 ignore_zero_division=True)  # 문제 없음

try:
    safe_division_c(1, 0)
except ZeroDivisionError:
    pass  # 기대한 대로 동작함
