import pickle


def filter_dump(filename: str, objects: list, typename):
    with open(filename, 'wb') as pickle_file:
        filtered_objects = list(filter(lambda x: isinstance(x, typename), objects))
        pickle.dump(filtered_objects, pickle_file)
