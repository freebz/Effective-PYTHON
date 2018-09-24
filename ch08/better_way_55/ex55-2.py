a = '\x07'
print(repr(a))

b = eval(repr(a))
assert a == b

print(repr(5))
print(repr('5'))

print('%r' % 5)
print('%r' % '5')
