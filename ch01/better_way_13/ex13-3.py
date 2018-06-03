# 모두 함께 사용하기

UNDEFINED = object()

def divide_json(path):
    handle = open(path, 'r+')   # IOError가 일어날 수 있음
    try:
        data = handle.read()    # UnicodeDecodeError가 일어날 수 있음
        op = json.loads(data)   # ValueError가 일어날 수 있음
        value = (
            op['numerator'] /
            op['denominator'])  # ZeroDivisionError가 일어날 수 있음
    except ZeroDivisionError as e:
        return UNDEFINED
    else:
        op['result'] = value
        result = json.dumps(op)
        handle.seek(0)
        handle.write(result)    # IOError가 일어날 수 있음
        return value
    finally:
        handle.close()          # 항상 실패함
