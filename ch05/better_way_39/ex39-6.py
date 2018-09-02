in_queue = Queue()

def consumer():
    print('Consumer waiting')
    work = in_queue.get()      # 두 번째로 완료함
    print('Consumer working')
    # 작업을 수행함
    # ...
    print('Consumer done')
    in_queue.task_done()       # 세 번째로 완료함

Thread(target=consumer).start()


in_queue.put(object())         # 첫 번째로 완료함
print('Producer waiting')
in_queue.join()
print('Producer done')

>>>
Consumer waiting
Producer waiting
Consumer working
Consumer done
Producer done
