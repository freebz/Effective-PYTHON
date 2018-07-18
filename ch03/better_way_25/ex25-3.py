class AnotherWay(MyBaseClass, PlusFive, TimesTwo):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)


bar = AnotherWay(5)
print('Second ordering still is', bar.value)

>>>
Second ordering still is 15
