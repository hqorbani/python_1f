import random
my_request = "y"
point = 100
while my_request == "y":
    a = random.randint(0 , 100)
    while point > 0:
        b = int(input ("pick a number: "))
        if a > b:
            print("it's small, guess a bigger number... ")
            point = point - 10
        elif a < b:
            print("it's big, guess a smaller number... ")
            point = point - 10
        else:
            print ("exellent you win!, your piont is", point)
            my_request = input("Do you want to paly again? (y/n) ")
            if my_request == "y":
                break
            else:
               point = 0
        # point = point - 10
    print("you lost!, the number was", a)
    my_request = input("Do you want to paly again? (y/n) ")
    if my_request == "y":
        point = 100
    else:
        break
#point = point - 10