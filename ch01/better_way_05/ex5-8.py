b = a
print('Before', a)
a[:] = [101, 102, 103]
assert a is b           # 여전히 같은 리스트 객체임
print('After ', a)      # 이제 다른 내용을 담음

>>> 
Before ['a', 'b', 99, 22, 14, 'h']
After  [101, 102, 103]
