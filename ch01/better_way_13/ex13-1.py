# finally 블록

handle = open('/tmp/random_data.txt')  # IOError가 일어날 수 있음
try:
    data = handle.read()  # UnicodeDecodeError가 일어날 수 있음
finally:
    handle.close()        # try: 이후에 항상 실행됨
