class CountMissing(object):
    def __init__(self):
        self.added = 0

    def missing(self):
        self.added += 1
        return 0


counter = CountMissing()
result = defaultdict(counter.missing, current)  # 메서드 참조

for key, amount in increments:
    result[key] += amount
assert counter.added == 2
