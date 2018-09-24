class BetterClass(object):
    def __init__(self, x, y):
        # ...

    def __repr__(self):
        return 'BetterClass(%d, %d)' % (self.x, self.y)


obj = BetterClass(1, 2)
print(obj)


obj = OpaqueClass(4, 5)
print(obj.__dict__)
