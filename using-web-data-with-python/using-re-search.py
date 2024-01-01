import re

hand = open('ladies.txt')
names = list()
for line in hand:
    line = line.rstrip()
    if re.search('Name: ', line):
        names.append(line)
print(names)