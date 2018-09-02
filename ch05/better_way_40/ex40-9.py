# 파이썬 2
def delegated():
    yield 1
    yield 2

def composed():
    yield 'A'
    for value in delegated():  # 파이선 3에서는 yield from
        yield value
    yield 'B'

print list(composed())

>>>
['A', 1, 2, 'B']
