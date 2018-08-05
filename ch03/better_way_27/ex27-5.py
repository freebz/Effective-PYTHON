class MyIntegerSubclass(MyClass):
    def get_value(self):
        return int(self._MyClass_value)

foo = MyIntegerSubclass(5)
assert foo.get_value() == 5
