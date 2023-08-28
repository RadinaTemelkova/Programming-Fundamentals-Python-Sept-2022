orders = {}
while True:
    command = input()
    if command == "buy":
        break
    current_command = command.split()
    name = current_command[0]
    price = float(current_command[1])
    quantity = int(current_command[2])

    if name not in orders.keys():
        orders[name] = [price, quantity]
    else:
        orders[name][0] = price
        orders[name][1] += quantity

for key, value in orders.items():
    product_price = value[0]
    product_quantity = value[1]
    total_product_price = product_price * product_quantity
    print(f"{key} -> {total_product_price:.2f}")





