# list
numbers = [154,321,12,23,35,63,230,251,21,238,659,250,522,2541,12,10,19,18]

#Dictionary

fruits = {
    "apple" : 6 ,
    "orange": 5,
    "lemon": 7,
    "melone": 15
    }
# print(fruits["lemon"])

fruits["coconat"] = 16

for item in fruits:
    print(item , fruits[item])


# while len(fruits) < 5:
for i in range(2):
    fruit_name = input("please enter your fruit name: ")
    fruit_price = input("please enter your fruit price: ")
    fruits[fruit_name] = fruit_price
print("/--------------")
for item in fruits:
    print(item , fruits[item])
