from more_itertools import partition

a = []
for line in open('day3.txt').read().split('\n'):
    a.append(line)

transposed = list(map(list, zip(*a)))


def most_common_bit(bits: list):
    ones, zeros = map(list, partition(lambda i: i == '0', bits))
    return '1' if len(list(ones)) >= len(list(zeros)) else '0'


def least_common_bit(bits: list):
    ones, zeros = map(list, partition(lambda i: i == '0', bits))
    return '1' if len(list(ones)) < len(list(zeros)) else '0'


gamma_rate = int("".join(list(map(most_common_bit, transposed))), 2)
epsilon_rate = int("".join(list(map(least_common_bit, transposed))), 2)
print(gamma_rate*epsilon_rate)
