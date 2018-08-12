r0 = OldResistor(50e3)
print('Before: %5r' % r0.get_ohms())
r0.set_ohms(10e3)
print('After: %5r' % r0.get_ohms())

>>>
Before: 50000.0
After: 10000.0


r0.set_ohms(r0.get_ohms() + 5e3)
