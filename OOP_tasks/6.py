# put your python code here
import sys


def filter_coord(coords: tuple) -> bool:
    x, y = eval(coords)
    return -90 <= x <= 90 and -180 <= y <= 180


for line in sys.stdin:
    print(filter_coord(line))
