# else 블록

def load_json_key(data, key):
    try:
        result_dict = json.loads(data)  # ValueError가 일어날 수 있음
    except ValueError as e:
        raise KeyError from e
    else:
        return result_dict[key]         # KeyError가 일어날 수 있음
