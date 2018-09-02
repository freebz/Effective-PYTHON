class ColumnPrinter(object):
    # ...

columns = ColumnPrinter()
sim = simulate(grid.height, grid.width)
for i in range(5):
    columns.append(str(grid))
    grid = live_a_generation(grid, sim)

print(columns)

>>>
    0    |    1    |    2    |    3    |    4
---*-----|---------|---------|---------|---------
----*----|--*-*----|----*----|---*-----|----*----
--***----|---**----|--*-*----|----**---|-----*---
---------|---*-----|---**----|---**----|---***---
---------|---------|---------|---------|---------
