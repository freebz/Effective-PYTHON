class Deserializable(Serializable):
    @classmethod
    def deserialize(cls, json_data):
        params = json.loads(json_data)
        return cls(*params['args'])

    
class BetterPoint2D(Deserializable):
    # ...


point = BetterPoint2D(5, 3)
print('Before:    ', point)
data = point.serialize()
print('Serialized:', data)
after = BetterPoint2D.deserialize(data)
print('After:     ', after)

>>>
Before:     BetterPoint2D(5, 3)
Serialized: {"args": [5, 3]}
After:      BetterPoint2D(5, 3)
