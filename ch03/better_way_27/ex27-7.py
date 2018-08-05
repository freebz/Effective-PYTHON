class MyClass(object):
    def __init__(self, value):
        # 사용자가 객체에 전달한 값을 저장한다.
        # 문자열로 강제할 수 있는 값이어야 하며,
        # 객체에 할당하고 나면 불변으로 취급해야 한다.
        self._value = value
