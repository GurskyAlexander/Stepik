from collections import ChainMap
import json


with open('zoo (1).json') as json_file:
    total = ChainMap(*json.load(json_file))
    print(sum(total.values()))
