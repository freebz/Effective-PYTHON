# 기본 딕셔너리

stats = {}
key = 'my_counter'
if key not in stats:
    stats[key] = 0
stats[key] += 1


from collections from defaultdict

stats = defaultdict(int)
stats['my_counter'] += 1
