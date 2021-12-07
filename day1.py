from more_itertools import windowed

a = []
for line in open('day1.txt').read().split('\n'):
    a.append(int(line))

print(sum(map(lambda a: 1 if a[0] < a[1] else 0, windowed(a, 2))))

print(sum(map(lambda a: 1 if a[0] < a[1] else 0, windowed(map(
    lambda a: a[0] + a[1] + a[2], windowed(a, 3)), 2))))
