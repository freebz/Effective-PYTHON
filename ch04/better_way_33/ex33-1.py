class Meta(type):
    def __new__(meta, name, bases, class_dict):
        print((meta, name, bases, class_dict))
        return type.__new__(meta, name, bases, class_dict)

class MyClass(object, metaclass=Meta):
    stuff = 123

    def foo(self):
        pass


>>>
(<class '__main__.Meta'>,
 'MyClass',
 (<class 'object'>,),
 {'__qualname__': 'MyClass',
  'foo': <function MyClass.foo at 0xb70a04f4>,
  'stuff': 123,
  '__module__': '__main__'})
