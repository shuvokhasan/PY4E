numlist = list()

while True:
    inp = input('Enter a number:')
    if inp == 'Done' : break
    value = float(inp)
    numlist.append(value)

avg = sum(numlist) / len(numlist)
print('Numbers:', numlist)
print('Average:', avg)