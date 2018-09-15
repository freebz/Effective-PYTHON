# 더블 엔디드 큐

from collections import deque

fifo = deque()
fifo.append(1)      # 생산자
x = fifo.popleft()  # 소비자
