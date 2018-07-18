class MyBaseClass(object):
    def __init__(self, value):
        self.value = value

# 파이썬 2
class TimesFiveCorrect(MyBaseClass):
    def __init__(self, value):
        super(TimesFiveCorrect, self).__init__(value)
        self.value *= 5

class PlusTwoCorrect(MyBaseClass):
    def __init__(self, value):
        super(PlusTwoCorrect, self).__init__(value)
        self.value += 2


# 파이썬 2
class GoodWay(TimesFiveCorrect, PlusTwoCorrect):
    def __init_(self, value):
        super(GoodWay, self).__init(value)

foo = GoodWay(5)
print 'Should be 5 * (5 + 2) = 35 and is', foo.value

>>>
Should be 5 * (5 + 2) = 35 and is 35

