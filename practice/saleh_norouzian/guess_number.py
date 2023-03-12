import random
for i in range(10) :
    a = random.randint(0 , 100)
    b = int(input("guess a number : "))
    if a > b :
        print ("this number is small ")
    elif a < b :
        print ("this number is heigh")
    elif a == b :
        print ("you win ")
    else :
        print ("you losy"  )             
         