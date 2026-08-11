foods = []
prices = []
total = 0

while True:
    food = input("Enter the food item (or type 'done' to finish: ")
    if food.lower() == 'done':
        break
    else:
        price = float(input(f"Enter the price for {food}: $"))
        foods.append(food)
        prices.append(price)

print("============== SHOPPING CART ==============")

for food in foods:
    print(food)

for price in prices:
    total += price
print("===========================================")
print(f"Total: ${total}")