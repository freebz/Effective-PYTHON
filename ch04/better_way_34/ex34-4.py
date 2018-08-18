class Point3D(BetterSerializable):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
        self.x = x
        self.y = y
        self.z = z

# 이런! register_class를 호출하는 일을 깜빡 잊었다!


point = Point3D(5, 9, -4)
data = point.serialize()
deserialized(data)

>>>
KeyError: 'Point3D'
