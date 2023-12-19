

def txt_to_dict():
    with open('planets.txt', encoding='utf-8') as file:
        block_gen = (block.split('\n') for block in file.read().split('\n\n'))
        d = (dict(map(lambda x: x.split(' = '), line)) for line in block_gen)
        yield  from d


txt_to_dict()