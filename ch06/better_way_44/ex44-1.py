import pickle

class GameState(object):
    def __init__(self):
        self.level = 0
        self.lives = 4


state = GameState()
state.level += 1  # 플레이어가 레벨을 통과함
state.lives -= 1  # 플레이어가 재도전해야 함


state_path = '/tmp/game_state.bin'
with open(state_path, 'wb') as f:
    pickle.dump(state, f)


with open(state_path, 'rb') as f:
    state_after = pickle.load(f)
print(state_after.__dict__)

>>>
{'lives': 3, 'level': 1}
