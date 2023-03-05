<<<<<<< HEAD
# tips and guide
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
'''
# sum of dictionary values
print(sum(fruits.values()))
# max of dictionary values
print(max(fruits.values()))
# min of dictionary values
print(min(fruits.values()))
'''
list_name = list(fruits.keys())
list_price = list(fruits.values())

#print(list_name)
#print(list_price)

# item with minimum price
mini_price = min(list_price)
mini_price_list = []
for i in list_name:
    if fruits[i] == mini_price:
        mini_price_list.append(i)
print("Price and item with minimum price:")
print(mini_price_list)
print(mini_price)

# item with maximum price
maxi_price = max(list_price)
maxi_price_list = []
for i in list_name:
    if fruits[i] == maxi_price:
        maxi_price_list.append(i)
print("Price and item with Maximum price:")
print(maxi_price)
print(maxi_price_list)

# jam-e price
print("Sum of all price:")
print(sum(list_price))

#kamtar Az Dah
kamtarAzdah = []
for i in list_price:
    if i < 10:
        kamtarAzdah.append(i)
jameKamtarAzDah = sum(kamtarAzdah)
miyanginKamtarAzDah = jameKamtarAzDah/len(kamtarAzdah)
print("jam va miyangin ajnas ba geymat kamtar az 10:")
print(jameKamtarAzDah)
print(miyanginKamtarAzDah)

#bishtar Az Dah
bishtarAzdah = []
for i in list_price:
    if i > 10:
        bishtarAzdah.append(i)
jameBishtarAzDah = sum(bishtarAzdah)
miyanginbishtarAzDah = jameBishtarAzDah/len(bishtarAzdah)
print("jam va miyangin ajnas ba geymat bishtar az 10:")
print(jameBishtarAzDah)
print(miyanginbishtarAzDah)
=======
# tips and guide
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
'''
# sum of dictionary values
print(sum(fruits.values()))

# max of dictionary values
print(max(fruits.values()))

# min of dictionary values
print(min(fruits.values()))
'''
list_name = list(fruits.keys())
list_price = list(fruits.values())

#print(list_name)
#print(list_price)

# item with minimum price
mini_price = min(list_price)
mini_price_list = []
for i in list_name:
    if fruits[i] == mini_price:
        mini_price_list.append(i)
print("Price and item with minimum price:")
print(mini_price_list)
print(mini_price)

# item with maximum price
maxi_price = max(list_price)
maxi_price_list = []
for i in list_name:
    if fruits[i] == maxi_price:
        maxi_price_list.append(i)
print("Price and item with Maximum price:")
print(maxi_price)
print(maxi_price_list)

# jam-e price
print("Sum of all price:")
print(sum(list_price))

#kamtar Az Dah
kamtarAzdah = []
for i in list_price:
    if i < 10:
        kamtarAzdah.append(i)
jameKamtarAzDah = sum(kamtarAzdah)
miyanginKamtarAzDah = jameKamtarAzDah/len(kamtarAzdah)
print("jam va miyangin ajnas ba geymat kamtar az 10:")
print(jameKamtarAzDah)
print(miyanginKamtarAzDah)

#bishtar Az Dah
bishtarAzdah = []
for i in list_price:
    if i > 10:
        bishtarAzdah.append(i)
jameBishtarAzDah = sum(bishtarAzdah)
miyanginbishtarAzDah = jameBishtarAzDah/len(bishtarAzdah)
print("jam va miyangin ajnas ba geymat bishtar az 10:")
print(jameBishtarAzDah)
print(miyanginbishtarAzDah)

>>>>>>> origin/master
