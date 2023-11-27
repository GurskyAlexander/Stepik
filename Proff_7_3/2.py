def add_to_list_in_dict(data: dict, key, element) -> None:
    try:
        data[key].append(element)
    except KeyError:
        data[key] = [element]