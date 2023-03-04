names = []
while len( names ) < 3 :
    name = input ( " please enter your name: " )
    age = int ( input ( " please enter your age: " ) )
    if 13 <= age <= 19 :
        names.append ( name ) 
print ( names )
print ( "finished" )