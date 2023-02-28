# this program can calculate the area and perimeter of triangle
# if height is greater than width it will calculate the area
# if the height is smaller than the width, it will calculate the perimeter

height = int(input("please enter height: "))
width = int(input("please enter width: "))
if height > width:
    area = height * width / 2
    print("area:" , area)
elif height < width:
    vatar = int(input("pelase enter vatar: "))
    perimeter = height + width + vatar
    print("perimeter:" , perimeter)
else:
    print("In this program, you can't enter height and width with the same size")
    print("you can run again to enter new data...")