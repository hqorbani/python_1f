pizzas = {
    "margarita" : 5,
    "pepperoni" : 6,
    "mix" : 5,
    }
tax = 9
request = 'y'
print("welcome ")
while request == 'y':
    for pizza_name , pizza_price in pizzas.items():
        print(pizza_name , pizza_price)
        # ux: user experince/ui user interface
    pizza_type = input("please enter your pizza name: ")
    if pizza_type in pizzas:
        pizza_number = int(input("how many?"))
        order_price = pizza_number * pizzas[pizza_type]
        payable_price = order_price + (order_price * tax / 100)
        print("order price: ", order_price)
        print("tax:" , tax,"%")
        print("payable price: ", payable_price)
    else:
        print("sorry , there is not")
    request = input("new order?")
