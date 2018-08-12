r3 = BoundedResistance(1e3)
r3.ohms = 0

>>>
ValueError: 0.000000 ohms must be > 0


BoundedResistance(-5)

>>>
ValueError: -5.000000 ohms must be > 0
