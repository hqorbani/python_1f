pizzas = {
    "margarita" : 5,
    "pepperoni" : 6,
    "mix" : 5
}
tax = 9
for pizza, price in pizzas.items():
    print(pizza, price)
order_pizza = input("chi meil darid? ")
pizza_number = int(input("sefaresheton baraye chand nafar ast? "))

for pizza in pizzas.keys():
    if pizza == order_pizza:
        pizza_price = pizzas[pizza]

all_pizza_price = pizza_price * pizza_number 
payable_price = all_pizza_price + (all_pizza_price * tax / 100)
print(payable_price)


