from collections import Counter


def print_bar_chart(data, mark):
    data = Counter(data)
    max_l = max(map(len, data))

    for key, value in data.most_common():
        count = mark * value
        print(f'{key.ljust(max_l)} |{count}')


a, b = ['java', 'java', 'python', 'C++', 'assembler', 'java', 'C++', 'C', 'pascal', 'C++', 'pascal', 'java'], '+'
print_bar_chart(a, b)
