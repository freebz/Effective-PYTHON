def run_md5(input_stdin):
    proc = subprocess.Popen(
        ['md5'],
        stdin=input_stdin,
        stdout=subprocess.PIPE)
    return proc


input_procs = []
hash_procs = []
for _ in range(3):
    data = os.urandom(10)
    proc = run_openssl(data)
    input_procs.append(proc)
    hash_proc = run_md5(proc.stdout)
    hash_procs.append(hash_proc)


for proc in input_procs:
    proc.communicate()

for proc in hash_procs:
    out, err = proc.communicate()
    print(out.strip())

>>>
b'8b351296638c6505d8023502149ebcd3  -'
b'e15843e981b95309e586b591cd56b7d5  -'
b'2b641d52098bd02083d1bec9ce2239a9  -'
