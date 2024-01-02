hand = open('testfile.txt')
# hand.write('\nThis line is created with python code.')
# hand.close()

# # open & read after appending
# f = open('testfile.txt', 'r')
# print(f.read())
words = list()
for line in hand:
    line = line.rstrip()
    # words = line.split()
    if line.find('HiThis ') >= 0:
        words = line.split()
print(words)