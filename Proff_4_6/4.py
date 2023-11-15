import pickle


def main():
    file_name: str = input()
    control_sum: int = int(input())
    answer = ['Контрольные суммы не совпадают', 'Контрольные суммы совпадают']

    with open(file_name, 'rb') as pickle_file:
        content = pickle.load(pickle_file)
        if isinstance(content, dict):
            new_sum = sum(filter(lambda x: isinstance(x, int), content.keys()))
            print(answer[control_sum == new_sum])
        else:
            new_list = list(filter(lambda x: isinstance(x, int), content))
            new_sum = max(new_list) * min(new_list) if new_list else 0
            print(answer[control_sum == new_sum])


if __name__ == '__main__':
    main()
