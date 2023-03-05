numbers = [154,321,12,23,35,63,230,251,21,238,659,250,522,2541,12,10,19,18]
bakhsh = []
jam_bakhsh = 0
for number in numbers :
    if number % 3 == 0 :
        bakhsh.append(number)
for number in bakhsh :
    jam_bakhsh = number + jam_bakhsh
miangin = jam_bakhsh / len(bakhsh)
print(miangin)