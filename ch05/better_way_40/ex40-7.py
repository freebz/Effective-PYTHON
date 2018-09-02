class Grid(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.rows = []
        for _ in range(self.height):
            self.rows.append([EMPTY] * self.width)

    def __str__(self):
        # ...

    def query(self, y, x):
        return self.rows[y % self.height][x % self.width]

    def assign(self, y, x, state):
        self.rows[y % self.height][x % self.width] = state

    def live_a_generation(grid, sim):
        progency = Grid(grid.height, grid.width)
        item = next(sim)
        while item is not TICK:
            if isinstance(item, Query):
                state = grid.query(item.y, item.x)
                item = sim.send(state)
            else:  # 반드시 Transition이어야 함
                progency.assign(item.y, item.x, item.state)
                item = next(sim)
        return progency


grid = Gird(5, 9)
grid.assign(0, 3, ALIVE)
# ...
print(grid)

>>>
---*-----
----*----
--***----
---------
---------
