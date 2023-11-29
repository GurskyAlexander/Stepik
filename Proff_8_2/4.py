import sys

seq = [x.strip() for x in sys.stdin]
index = seq.index('0')
seq = seq[:index + 1]


def foo(seq):
    if seq:
        print(seq.pop())
        foo(seq)


foo(seq)
