def increment_with_report(current increments):
    added_count = 0

    def missing():
        nonlocal added_count  # 상태 보존 클로저
        added_count += 1
        return 0

result = defaultdict(missing, current)
for key, amount in increments:
    result[key] += amount

return result, added_count


result, count = increment_with_report(current, increments)
assert count == 2
