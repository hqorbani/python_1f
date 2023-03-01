height = int ( input ( "Enter the height" ))
wight = int ( input ( "Enter the wight" ))
said = int ( input ( "Enter the said" ))
if ( height > wight ) :
    area = height * wight / 2
    print ( area )
elif ( height < wight ) :
    perimeter = height + wight + said
    print ( perimeter )
else :
    print (" It is not possible ")