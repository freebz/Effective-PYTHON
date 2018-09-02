from queue import Queue
queue = Queue()

def consumer():
    print('Consumer waiting')
    queue.get()                # 뒤에 나오는 put() 이후에 실행함
    print('Consumer done')

thread = Thread(target=consumer)
thread.start()


print('Producer putting')
queue.put(object())            # 앞에 나온 get() 이전에 실행함
thread.join()
print('Producer done')

>>>
Consumer waiting
Producer putting
Consumer done
Producer done
