import re

bought_furniture = []
total_cost = 0

while True:
    furniture = input()
    if furniture == "Purchase":
        break
    pattern = r">>([A-Za-z]+)<<([0-9]+\.?[0-9]*)!([0-9]+)"
    valid_info = re.search(pattern, furniture)
    if valid_info:
        furniture = valid_info.group(1)
        bought_furniture.append(furniture)

        price = float(valid_info.group(2))
        quantity = int(valid_info.group(3))
        total_cost += price * quantity

print("Bought furniture:")
for item in bought_furniture:
    print(item)
print(f"Total money spend: {total_cost:.2f}")
