a = []
for line in open('day2.txt').read().split('\n'):
    a.append(line)

h = 0
d = 0

for i in a:
    op = i.split(" ")[0]
    n = int(i.split(" ")[1])
    if (op == 'forward'):
        h += n
    elif (op == 'up'):
        d -= n
    elif (op == 'down'):
        d += n

print(h*d)

h = 0
d = 0
aim = 0

for i in a:
    op = i.split(" ")[0]
    n = int(i.split(" ")[1])
    if (op == 'forward'):
        h += n
        d += aim * n
    elif (op == 'up'):
        aim -= n
    elif (op == 'down'):
        aim += n

print(h*d)
