print(2, '\n', 3, sep='')
for number in range(4, 1000000):
    for factor in range(2, int(number ** 0.5)+1):
        if number % factor == 0:
            break
        if factor == int(number ** 0.5):
            print(number)
