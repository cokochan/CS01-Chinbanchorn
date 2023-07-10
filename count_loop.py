count = 0
for number in range(int(input('input:'))):
    if number % 2 != 0:
        count += 1
        print(number, end=" ")
print(f'We have {count} odd numbers')