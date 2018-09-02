queue = Queue(1)               # 크기가 1인 버퍼

def consumer():
    time.sleep(0.1)            # 대기
    queue.get()                # 두 번째로 실행함
    print('Consumer got 1')
    queue.get()                # 네 번째로 실행함
    print('Consumer got 2')

thread = Thread(target=consumer)
thread.start()


queue.put(object())            # 첫 번째로 실행함
print('Producer put 1')
queue.put(object())            # 세 번째로 실행함
print('Producer put 2')
thread.join()
print('Producer done')

>>>
Producer put 1
Consumer got 1
Producer put 2
Consumer got 2
Producer done
