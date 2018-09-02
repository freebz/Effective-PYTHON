class MyQueue(object):
    def __init__(self):
        self.items = deque()
        self.lock = Lock()

    def get(self):
        with self.lock:
            return self.items.popleft()
