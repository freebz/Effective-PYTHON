# 파이선 2의 키워드 전용 변수

# 파이썬 2
def print_args(*args, **kwargs):
    print 'Positional:', args
    print 'Keyword:   ', kwargs

print_args(1, 2, foo='bar', stuff='meep')

>>>
Positional: (1, 2)
Keyword:    {'foo': 'bar', 'stuff': 'meep'}
