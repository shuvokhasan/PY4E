# fname = input("Enter file name: ")
words = list()
fh = open('romeo.txt')
for line in fh:
    words = line.split()
    for word in words:
        if word in words:
            continue
        words.append(word)

print(sorted(words))