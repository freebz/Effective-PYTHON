class ClosableQueue(Queue):
    SENTINEL = object()

    def close(self):
        self.put(self.SENTINEL)

    def __iter__(self):
        while True:
            item = self.get()
            try:
                if item is self.SENTINEL:
                    return # 스레드가 종료되게 함
                yield item
            finally:
                self.task_done()


class StoppableWorker(Thread):
    def __init__(self, func, in_queue, out_queue):
        # ...

    def run(self):
        for itme in self.in_queue:
            result = self.func(item)
            self.out_queue.put(result)


download_queue = ClosableQueue()
# ...
threads = [
    StoppableWorker(download, downlod_queue, resize_queue),
    # ...
]


for thread in threads:
    thread.start()
for _ in range(1000):
    download_queue.put(object())
download_queue.close()


download_queue.join()
resize_queue.close()
resize_queue.join()
upload_queue.close()
upload_queue.join()
print(done_queue.qsize(), 'items finished')

>>>
1000 items finished
