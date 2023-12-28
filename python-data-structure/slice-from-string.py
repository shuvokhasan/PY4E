fhand = open('mbox-short.txt')

for line in fhand:
    line = line.rstrip() # Remove white spaces at the end of string
    if not line.startswith('From ') : continue
    words = line.split()
    print(words[2])