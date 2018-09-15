# 정렬된 딕셔너리

from random import randint

a = {}
a['foo'] = 1
a['bar'] = 2

# 무작위로 'b'에 데이터를 추가해서 해시 충돌을 일으킴
while True:
    z = randint(99, 1013)
    b = {}
    for i in range(z):
        b[i] = i
    b['foo'] = 1
    b['bar'] = 2
    for i in range(z):
        del b[i]
    if str(b) != str(a):
        break

print(a)
print(b)
print('Equal?', a == b)

>>>
{'foo': 1, 'bar': 2}
{'bar': 2, 'foo': 1}
Equal? True
