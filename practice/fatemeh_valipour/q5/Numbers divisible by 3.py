numbers = [154,321,12,23,35,63,230,251,21,238,659,250,522,2541,12,10,19,18]
divisible_numbers = []

for number in numbers :
    if number % 3 == 0:
        divisible_numbers.append ( number )
print(divisible_numbers)