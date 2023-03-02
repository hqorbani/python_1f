numbers = [51,65,9,54,65,21,656,542,54,32,51,120]
even_numbers = []
odd_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)
print("even numbers:",even_numbers)
print("odd numbers:",odd_numbers)