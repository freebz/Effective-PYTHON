def my_coroutine():
    while True:
        received = yield
        print('Received:', received)

it = my_coroutine()
next(it)             # 코루틴을 준비함
it.send('First')
it.send('Second')

>>>
Received: First
Received: Second
