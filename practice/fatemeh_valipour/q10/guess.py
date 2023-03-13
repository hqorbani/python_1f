import random
a = random . randint( 0 , 100 )
for i in range( 100 , 0 , -10 ) :
    print ( i )
    b = float(input ( " guess a number: " ))
    if a > b :
        print( " This number is small " ) 
    elif a < b :
        print ( " This number is high " )
    elif a == b :
        print ( " you win! " )
        break
if a != b :
    print ( " you lost! ", "the number was" a )
