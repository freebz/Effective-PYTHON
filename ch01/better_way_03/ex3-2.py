# 파이썬 2
def to_unicode(unicode_or_str):
    if isinstance(unicode_or_str, str):
        value = unicode_or_str.decode('utf-8')
    else:
        value = unicode_or_str
    return value  # unicode 인스턴스


# 파이썬 2
def to_str(unicode_or_str):
    if isinstance(unicodde_or_str, unicode):
        value = unicode_or_str.encode('utf-8')
    else:
        value = unicode_or_str
    return value  # str 인스턴스
