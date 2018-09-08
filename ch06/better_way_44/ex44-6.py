class BetterGameState(object):
    def __init__(self, level=0, points=0, magic=):
        # ...


pickle.loads(serialized)

>>>
AttributeError: Can't get attribute 'GameState' on <module '__main__' from 'my_code.py'>


print(serialized[:25])

>>>
b'\x80\x03c__main__\nGameState\nq\x00)'


copyreg.pickle(BetterGameState, pickle_game_state)


state = BetterGameState()
serialized = pickle.dumps(state)
print(serialized[:35])

>>>
b'\x80\x03c__main__\nnupickle_game_state\nq\x00}'
