class Meta(type):
    def __new__(meta, name, bases, class_dict):
        for key, value in class_dict.items():
            if isinstance(value, Field):
                value.name = key
                value.internal_name = '_' + key
        cls = type.__new__(meta, name, bases, class_dict)
        return cls


class DatabaseRow(object, metaclass=Meta):
    pass


class Field(object):
    def __init__(self):
        # 메타클래스가 이 속성들을 할당함
        self.name = None
        self.internal_name = None
    # ...


class BetterCustomer(DatabaseRow):
    first_name = Field()
    last_name = Field()
    prefix = Field()
    suffix = Field()


foo = BetterCustomer()
print('Before:', repr(foo.first_name), foo.__dict__)
foo.first_name = 'Euler'
print('After: ', repr(foo.first_name), foo.__dict__)

>>>
Before: '' {}
After:  'Euler' {'first_name': 'Euler'}
