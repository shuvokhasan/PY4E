hand = open('ladies.txt')
names = list()
for line in hand:
    line = line.rstrip()
    if line.find('Name:') >= 0:
        # print(line)
        name = line[6:]
        if len(line) != 0:
            names.append(name)

# removes empty names
for name in names:
    if len(name) < 3:
        names.remove(name)
print(names)