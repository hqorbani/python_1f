pizzas = {
    "margarita" : 5,
    "pepperoni" : 6,
    "mix" : 5,
    }
tax = 9
request = 'yes'
print("welcome ")
while request == 'yes':
    for pizza_name , pizza_price in pizzas.items():
        print(pizza_name , pizza_price)
    pizza_type = input("please enter your pizza name: ")
    if pizza_type in pizzas:
        pizza_number = int(input("please enter the number: "))
        order_price = pizza_number * pizzas[pizza_type]
        payable_price = order_price + (order_price * tax / 100)
        print("order price: ", order_price)
        print("tax:" , tax,"%")
        print("payable price: ", payable_price)
    else:
        print(" sorry, it cannot be done ")
    request = input(" do you have another order? ")
print (" Thank you for your order ")