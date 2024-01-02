import re

# extracting numbers from file
fhand = open('regex_sum_1796662.txt')
sample = fhand.read()
numbers = re.findall('[0-9]+', sample)
print(numbers)
# counting numbers
sum = 0
for number in numbers:
    number = int(number)
    sum = sum + number
print(sum)