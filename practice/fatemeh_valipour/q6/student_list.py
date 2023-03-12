for item in range(3) :
    student = {}
    student_number = int ( input ( " please enter your student number: " ))
    first_name = input ( " please enter your first name: " )
    last_name = input ( " plese enter your last name: " )
    student [ "student_number" ] = student_number
    student [ "first_name" ] = first_name
    student [" last_name "] = last_name
    for key , value in student. items():
        print ( key , value )