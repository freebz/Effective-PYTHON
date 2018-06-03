def sort_priority2(numbers, group):
    found = False         # 스코프: 'sort_priority2'
    def helper(x):
        if x in group:
            found = True  # 스코프: 'helper' -- 안 좋음!
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found
