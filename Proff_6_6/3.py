from collections import OrderedDict


def custom_sort(ordered_dict: OrderedDict, by_values=False) -> None:
    if not by_values:
        for key in sorted(ordered_dict):
            ordered_dict[key] = ordered_dict.pop(key)
    else:
        for key, value in sorted(ordered_dict.items(), key=lambda x: x[1]):
            ordered_dict[key] = ordered_dict.pop(key)


data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)
custom_sort(data, True)

print(data)
