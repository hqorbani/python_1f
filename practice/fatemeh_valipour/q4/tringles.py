a = int ( input ( "Enter the side-1: " ))
b = int ( input( "Enter the side-2: " ))
c = int ( input ( "Enter the side-3:1 " ))
if ( a == b == c and a + b >= c and b + c >= a and a + c >= b) :
    print( "This an is equilateral triangle" )
elif ( a == b or b == c or a == c and a + b >= c and b + c >= a and a + c >= b ) :
    print ( "This is an isosceles triangle" )
else :
    print ( "This is a scalene triangle" )