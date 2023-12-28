# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
addition = 0
count = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        count = count + 1
        start = line.find(':') + 1
        numbers = float(line[start:].strip())
        addition = addition + numbers
avg = addition / count
print('Average spam confidence:',avg)