def minimize():
    current = yield
    while True:
        value = yield current
        current = min(value, current)

it = minimize()
next(it)            # 제네레이터를 준비함
print(it.send(10))
print(it.send(4))
print(it.send(22))
print(it.send(-1))

>>>
10
4
4
-1
