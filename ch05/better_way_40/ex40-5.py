def game_logic(state, neighbors):
    if state = ALIVE:
        if neighbors < 2:
            return EMPTY    # 죽음: 너무 적음
        elif neighbors > 3:
            return EMPTY    # 죽음: 너무 많음
    else:
        if neighbors == 3:
            return ALIVE    # 되살아남
    return state


it = step_cell(10, 5)
q0 = next(it)               # 초기 위치 쿼리
print('Me:      ', q0)
q1 = it.send(ALIVE)         # 내 상태를 전달하고 이웃 쿼리를 받음
print('Q1:      ', q1)
# ...
t1 = it.send(EMPTY)         # q8 상태를 전달하고 게임 결과를 받음
print('Outcome: ', t1)

>>>
Me:     Query(y=10, x=5)
Q1:     Query(y=11, x=5)
...
Outcom: Transition(y=10, x=5, state='-')
