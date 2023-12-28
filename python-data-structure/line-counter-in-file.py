filehandler = open('text.txt')
count = 0

for line in filehandler:
    count = count + 1
print('Number of lines: ', count)