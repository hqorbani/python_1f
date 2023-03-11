pizzas = {
    "margarita" : 5,
    "pepperoni" : 6,
    "mix" : 5
    }
print(pizzas)
sefaresh = input("which pizza do you want? : ")
tedad = int(input("how many pizzas do you want? : "))
if sefaresh == "margarita" :
    price = pizzas.get("margarita") * tedad
elif sefaresh == "pepperoni" :
    price = pizzas.get("pepperoni") * tedad
elif sefaresh == "mix" :
    price = pizzas.get("mix") * tedad
else : 
    print("this pizzas in unavailable")
tax = 9
total = price + (price * tax / 100)
print(("total : ") , total)
