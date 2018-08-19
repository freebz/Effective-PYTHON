proc = subprocess.Popen(['sleep', '0.3'])
while proc.poll() is None:
    print('Working...')
    # 시간이 걸리는 작업 몇 개를 수행함
    # ...
print('Exit status', proc.poll())

>>>
Working...
Working...
Exit status 0
