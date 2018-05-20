random_bits = 0
for i in range(64):
    if randint(0, 1):
        random_bits |= 1 << i
