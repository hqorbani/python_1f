# for i in range(3,9):
#     print(i)
names = []
while len(names) < 3:
    name = input("please enter  yuor name: ")
    age = int(input("please enter  yuor age: "))
    if 13 <= age <= 19:
        names.append(name)
print(names)
