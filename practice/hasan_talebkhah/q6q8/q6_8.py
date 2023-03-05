#
list = []
for i in range(3):
    id_number = int(input("please Enter ID: "))
    name = input("please Enter Name: ")
    LastName = input("please enter last name: ")
    dic = {
        "ID Number" : id_number,
        "First Name" : name,
        "Last Name" : LastName
    }
    list.append(dic)
stu1 = list[0]
stu2 = list[1]
stu3 = list[2]
#
'''
print(stu1)
print(stu1.values())
x = list(stu1.values())
print(x)
for i in range(0,3):
    x = list(stu1.values())
    print(x[i])
for i in range(0,3):
    x = list(stu2.values())
    print(x[i])
for i in range(0,3):
    x = list(stu3.values())
    print(x[i])
'''


print(stu1)
print(stu2)
print(stu3)