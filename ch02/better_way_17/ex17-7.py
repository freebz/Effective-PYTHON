def normalize_defensive(numbers):
    if iter(numbers) is iter(numbers):  # 이터레이터 -- 거부!
        raise TypeError('Must supply a container')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


visits = [15, 35, 80]
normalize_defensive(visits)  # 오류 없음
visits = ReadVisits(path)
normalize_defensive(visits)  # 오류 없음


it = iter(visits)
normalize_defensive(it)

>>>
TypeError: Must supply a container
