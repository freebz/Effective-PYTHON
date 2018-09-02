download_queue = MyQueue()
resize_queue = MyQueue()
upload_queue = MyQueue()
done_queue = MyQueue()
threads = [
    Worker(download, download_queue, resize_queue),
    Worker(resize, resize_queue, upload_queue),
    Worker(upload, upload_queue, done_queue),
]


for thread in threads:
    thread.start()
for _ in range(1000):
    download_queue.put(object())


while len(done_queue.items) < 1000:
    # 기다리는 동안 유용한 작업을 수행함
    # ...



processed = len(done_queue.items)
polled = sum(t.polled_count for t in threads)
print('Processed', processed, 'items after polling',
      polled, 'times')

>>>
Processed 1000 items after polling 3030 times
