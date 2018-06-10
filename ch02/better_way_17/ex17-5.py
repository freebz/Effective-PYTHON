def normalize_func(get_iter):
    total = sum(get_iter())   # 새 이터레이터
    result = []
    for value in get_iter():  # 새 이터레이터
        percent = 100 * value / total
        result.append(percent)
    return result


percentages = normalize_func(lambda: read_visits(path))
