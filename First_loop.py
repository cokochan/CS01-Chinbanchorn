successful = True
for number in range(3):
    print('Attempt',number+1)
    if successful:
        print('Successful')
        break
else:
    print('Attempted 3 times and failed')
for x in range(5):
    for y  in range(2):
        print(f'({x},{y})')

for number in rang(1,10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f'We have {count} even numbers')