for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count
