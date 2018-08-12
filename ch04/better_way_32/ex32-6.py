class SavingDB(object):
    def __setattr__(self, name, value):
        # 몇몇 데이터를 DB 로그로 저장함
        # ...
        super().__setattr__(name, value)


class LoggingSavingDB(SavingDB):
    def __setattr__(self, name, value):
        print('Called __setttr__(%s, %r)' % (name, value))
        super().__setattr__(name, value)

data = LoggingSavingDB()
print('Before: ', data.__dict__)
data.foo = 5
print('After:  ', data.__dict__)
data.foo = 7
print('Finally:', data.__dict__)

>>>
Before:  {}
Called __setttr__(foo, 5)
After:   {'foo': 5}
Called __setttr__(foo, 7)
Finally: {'foo': 7}
