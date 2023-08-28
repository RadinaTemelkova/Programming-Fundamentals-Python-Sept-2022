resources_dict = {}
while True:
    command = input()
    if command == "stop":
        break

    quantity = int(input())

    if command in resources_dict.keys():
        resources_dict[command] += quantity
    else:
        resources_dict[command] = quantity
for key, quantity in resources_dict.items():
    print(f"{key} -> {quantity}")
