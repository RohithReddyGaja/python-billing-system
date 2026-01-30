items = []
prices = []
total = 0

while True:
    item = input("enter the items(q to quit): ")
    if item.lower()== "q" :
        break
    else:
        price = int(input(f"enter the price of {item}: $"))
        items.append(item)
        prices.append(price)
print("-------------your cart----------------")
for i in range(len(items)):
    print(f"{items[i]} - ${prices[i]}")

for price in prices:
    total += price
print("--------------------------------------")
print(f"your total will be ${total} ")