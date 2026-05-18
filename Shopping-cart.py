# Shopping cart exercise

items = []
quantity = []
prices = []
total = 0

while True:
    item = input("Enter a item to add to cart (q to quit): ")
    if item.lower() == "q":
        break
    else:
        quan = int(input(f"Enter the quantity of {item}: "))
        price = float(input(f"Enter the price of the {item}: Rs"))
        price = quan*price
        items.append(item)
        prices.append(price)

print("----- YOUR CART -----")

for item in items:
    print(item, end=" ")

for price in prices:
    total += price

print()
print(f"Your total is: Rs{total}")
