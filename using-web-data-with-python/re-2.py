import re

# greedy method
text = 'From: Using the : character'
y = re.findall('^F.+:', text)
print(y)