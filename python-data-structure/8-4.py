wordlist = []
fh = open('romeo.txt')
for line in fh:
    words = line.split()
    for word in words:
        if word in wordlist:
            continue
        wordlist.append(word)
print(sorted(wordlist))