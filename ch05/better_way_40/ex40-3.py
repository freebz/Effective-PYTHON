from collections import namedtuple

Query = namedtuple('Query', ('y', 'x'))


def count_neighbors(y, x):
    n_ = yield Query(y + 1, x + 0)  # 북쪽
    ne = yield Query(y + 1, x + 1)  # 북동쪽
    # e_, se, s_, sw, w_, nw ... 정의
    # ...
    neighbor_states = [n_, ne, e_, se, s_, sw, w_, nw]
    count = 0
    for state in neighbor_states:
        if state == ALIVE:
            count += 1
    return count


it = count_neighbors(10, 5)
q1 = next(it)                 # 첫 번째 쿼리를 받음
print('First yield: ', q1)
q2 = it.send(ALIVE)           # q1 상태를 보내고 q2를 받음
print('Second yield: ', q2)
q3 = it.send(ALIVE)           # q2 상태를 보내고 q3를 받음
# ...
try:
    count = it.send(EMPTY)    # Send q8 상태를 보내고 count를 받음
except StopIteration as e:
    print('Coun: ', e.value)  # return 문으로 반환한 값

>>>
First yield:  Query(y=11, x=5)
Second yield: Query(y=11, x=6)
...
Count: 2
