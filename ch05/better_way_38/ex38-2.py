counter.count += offset


value = getattr(counter, 'count')
result = value + offset
setattr(counter, 'count', result)


# 스레드 A에서 실행함
value_a = getattr(counter, 'count')
# 스레드 B로 컨텍스트를 전환함
value_b = getattr(counter, 'count')
result_b = value_b + 1
setattr(counter, 'count', result_b)
# 스레드 A로 컨텍스트를 되돌림
result_a = value_a + 1
setattr(counter, 'count', result_a)
