pizza = {}
rq = 'y'
while rq == 'y':
    pizza_name = input("please enter new pizza name: ")
    pizza_price = float(input("please enter new pizza price: "))
    pizza[pizza_name] = pizza_price
    print("your pizza registred into dic")
    rq = input("would you like register new pizza? ")
print()
print("pizza menu: ")
for k,j in pizza.items():
    print(k , j)