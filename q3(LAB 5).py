count = 0
number = 0
while count < 4:
    if number % 2 != 0:
        number += 1
        continue
    print(number)
    count += 1
    number += 1
