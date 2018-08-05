class ApiClass(object):
    def __init__(self):
        self._value = 5

    def get(self):
        return self._value

class Child(ApiClass):
    def __init__(self):
        super().__init__()
        self._value = 'hello'  # 충돌

a = Child()
print(a.get(), 'and', a._value, 'should be different')

>>>
hello and hello should be different
