with open(state_path, 'rb') as f:
    state_after = pickle.load(f)
print(state_after.__dict__)

>>>
{'level': 1, 'lives': 3}


assert isinstance(state_after, GameState)
