import random
for i in range( 10 ) :
    a = random . randint( 0 , 100 )
    b = float(input ( " guess a number: " ))
    if a > b :
        print( " This number is small " ) 
    elif a < b :
        print ( " This number is high " )
    elif a == b :
        print ( " you win! " )
    else :
        print ( " you lost! ", a )