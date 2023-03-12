sum_numbers = {}
average = {}
fruits = {
    "apple" : 6 ,
    "orange" : 5.5 ,
    "banana" : 11 ,
    "grapes" : 6 ,
    "coconat" : 14 ,
    "lemon" : 4.5 ,
    "melone" : 10 ,
    "kiwi" : 4.5 ,
    "cherry" : 6 ,
    "papaya" : 11,
    "pineapple" : 14 ,
    "watermelon" : 7 ,
    "avacado" : 13
}

sum_price = sum(fruits.values())
print("sum_price:", sum_price )

max_price = max( fruits.values())
print("max_price:" , max_price )

min_price = min ( fruits.values() )
print( "min_price:" , min_price ) 

average_price = sum_price/ len(fruits)
print( "average_price:", average_price )

for fruit_name , fruit_price in fruits.items():
    if fruit_price == max_price :
        print ( "max:", fruit_name , fruit_price )
    elif fruit_price == min_price :
        print ("min:", fruit_name , fruit_price )
numbers_10 = 6, 5.5, 6, 4.5, 4.5, 6, 7 
sum_10 = sum( numbers_10 )
sum_numbers[numbers_10] = sum_10
print ( sum_numbers )
numbers_11 = 11, 14, 11, 14, 13
average_11 = sum(numbers_11)/5
average[numbers_11] = average_11
print ( average )
