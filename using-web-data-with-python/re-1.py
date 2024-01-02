import re

# extracting numbers from text
text = 'My 2 favorite numbers are 19 and 42'
numbers = re.findall('[0-9]+', text)
print(numbers)