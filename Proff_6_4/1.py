from collections import namedtuple
import pickle

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])

with open('data.pkl', 'rb') as pickle_file:
    data = pickle.load(pickle_file)
    for row in data:
        for key, value in zip(Animal._fields, row):
            print(f'{key}: {value}')
        print()
