def log(sequence, message, *values):
    if not values:
        print('%s: %s' % (sequence, message))
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s: %s' % (sequence, message, values_str))


log(1, 'Favorites', 7, 33)      # 새로운 용법은 OK
log('Favorite numbers', 7, 33)  # 오래된 용법은 제대로 도앚ㄱ하지 않음

>>>
1: Favorites: 7, 33
Favorite numbers: 7: 33
