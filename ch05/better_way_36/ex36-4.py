def run_openssl(data):
    env = os.environ.copy()
    env['password'] = b'\xe24U\n\xd0Ql3S\x11'
    proc = subprocess.Popen(
        ['openssl', 'enc', '-des3', '-pass', 'env:password'],
        env=env,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE)
    proc.stdin.write(data)
    proc.stdin.flush()  # 자식 프로세스가 입력을 반드시 받게 함
    return proc


procs = []
for _ in range(3):
    data = os.urandom(10)
    proc = run_openssl(data)
    procs.append(proc)


for proc in procs:
    out, err = proc.communicate()
    print(out[-10:])

>>>
b' \x8b\xa1\x87\x1d\xa7X\xda\x88\xc9'
b')o\x17^\x03\xa2\xb3\xe6&='
b'\xa7\x8a\xf6\xa4\xa7\x9f\xa9\x88\x85h'
