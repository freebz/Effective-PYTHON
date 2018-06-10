def log(message, *values):  # 유일하게 다른 부분
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))


log('My numbers are', 1, 2)
log('Hi there')  # 훨씬 나음

>>>
My numbers are: 1, 2
Hi there
