def sort_priority2(numbers, group):
    found = False
    def helper(x):
        if x in group:
            found = True  # 간단해 보임
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found
