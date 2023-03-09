# tips and guide
fruits = {
    "apple" : 6 ,
    "orange" : 5.5 ,
    "banana" : 11 ,
    "grapes" : 6 ,
    "coconut" : 14 ,
    "lemon" : 4.5 ,
    "melone" : 10 ,
    "kiwi" : 4.5 ,
    "cherry" : 6 ,
    "papaya" : 11,
    "pineapple" : 14 ,
    "watermelon" : 7 ,
    "avacado" : 13
}
# sum of dictionary values
sum_price = sum(fruits.values())
print("sum price:", sum_price)

# max of dictionary values
max_price = max(fruits.values())
print("max price:", max_price)
# min of dictionary values
min_price = min(fruits.values())
print("min price:",min_price)
print("------------------")

for fruit_name , fruit_price in fruits.items():
    if fruit_price == max_price:
        print("max:", fruit_name , fruit_price)
        print("------------------")
    elif fruit_price == min_price:
        print("min:",fruit_name , fruit_price)


