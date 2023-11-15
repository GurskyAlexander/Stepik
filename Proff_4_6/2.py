import pickle
import sys

file_name = input()

with open(file_name, 'rb') as p_file:
    foo = pickle.load(p_file)

arguments = [x.strip() for x in sys.stdin]
print(foo(*arguments))
