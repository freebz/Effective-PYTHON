from threading import Lock

lock = Lock()
with lock:
    print('Lock is held')
    

lock.acquire()
try:
    print('Lock is held')
finally:
    lock.release()
