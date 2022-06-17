from xmlrpc.client import Boolean
from bitarray import bitarray

a = []
for line in open('day3.txt').read().split('\n'):
    a.append(bitarray(line))

gamma_rate = bitarray()
epsilon_rate = bitarray()

for i in range(len(a[0])):
    zeros = 0
    ones = 0

    for j in range(len(a)):
        if a[j][i] == 0:
            zeros += 1
        else:
            ones += 1

    if zeros < ones:
        gamma_rate.append(1)
        epsilon_rate.append(0)
    else:
        gamma_rate.append(0)
        epsilon_rate.append(1)

print(int(gamma_rate.to01(), 2)*int(epsilon_rate.to01(), 2))


def rating_from_report(report, most_common: Boolean):
    numbers = report
    for i in range(len(numbers[0])):
        zeros = 0
        ones = 0

        if(len(numbers)) == 1:
            break
        else:
            for j in range(len(numbers)):
                if numbers[j][i] == 0:
                    zeros += 1
                else:
                    ones += 1

            if zeros <= ones:
                numbers = list(
                    filter(lambda number: number[i] == (1 if most_common else 0), numbers))
            else:
                numbers = list(
                    filter(lambda number: number[i] == (0 if most_common else 1), numbers))

    return int(numbers[0].to01(), 2)


print(rating_from_report(a, True)*rating_from_report(a, False))
