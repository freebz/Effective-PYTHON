class GameState(object):
    def __init__(self):
        # ...
        self.points = 0


state = GameState()
serialized = pickle.dumps(state)
state_after = pickle.loads(serialized)
print(state_after.__dict__)

>>>
{'lives': 3, 'level': 1, 'points': 0}
