# 파이썬 2
class Meta(type):
    def __new__(meta, name, bases, class_dict):
        # ...

class MyClassInPython2(object):
    __metaclass__ = Meta
    # ...
