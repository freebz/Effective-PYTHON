from heapq import *

a = []
heappush(a, 5)
heappush(a, 3)
heappush(a, 7)
heappush(a, 4)
assert a[0] == nsmallest(1, a)[0] == 3


print('Before:', a)
a.sort()
print('After: ', a)

>>>
Before: [3, 4, 7, 5]
After:  [3, 4, 5, 7]
