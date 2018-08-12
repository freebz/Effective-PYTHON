r2 = VoltageResistance(1e3)
print('Before: %5r amps' % r2.current)
r2.voltage = 10
print('After: %5r amps' % r2.current)

>>>
Before:     0 amps
After:  0.01 amps
