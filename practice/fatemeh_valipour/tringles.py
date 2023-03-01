a = int ( input ( "Enter the side-1" ))
b = int ( input( "Enter the side-2" ))
c = int ( input ( "Enter the side-3" ))
if ( a == b, b == c , a + b >= c , b + c >= a , a + c >= b) :
    print( "This an is equilateral triangle" )
elif ( a == b , a + b >= c , b + c >= a , a + c >= b ) :
    print ( "This is an isosceles triangle" )
else :
    print ( "This is a scalene triangle" )