for i in range(3):
    student = {}
    id = input("please enter your id: ")
    name = input("please enter your name: ")
    family = input("please enter your family: ")
    student["id"] = id
    student["name"] = name
    student["family"] = family
    for key , value in student.items():
        print(key, value)    