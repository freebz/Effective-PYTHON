class BetterCountMissing(object):
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0

counter = BetterCountMissing()
counter()
assert callable(counter)


counter = BetterCountMissing()
result = defaultdict(counter, current)  # __call__이 필요함
for key, amount in increments:
    result[key] += amount
assert counter.added == 2
