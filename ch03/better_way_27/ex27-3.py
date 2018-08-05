class MyParentObject(object):
    def __init__(self):
        self.__private_field = 71

class MyChildObject(MyParentObject):
    def get_private_field(self):
        return self.__private_field

baz = MyChildObject()
baz.get_private_field()

>>>
AttributeError: 'MyChildObject' object has no attribute '_MyChildObject__private_field'


assert baz._MyParentObject__private_field == 71

print(baz.__dict__)

>>>
{'_MyParentObject__private_field': 71}
