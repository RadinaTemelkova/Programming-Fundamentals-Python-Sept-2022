decorations_quantity = int(input())
days_left = int(input())
points = 0
total_price = 0
price_ornament_set = 2
price_tree_skirt = 5
price_tree_garland = 3
price_tree_lights = 15
points_ornament_set = 5
points_tree_skirt = 3
points_tree_garland = 10
points_tree_lights = 17
for current_day in range(1, days_left+1):

    if current_day % 11 == 0:
        decorations_quantity += 2

    if current_day % 2 == 0:
        points += points_ornament_set
        total_price += price_ornament_set * decorations_quantity

    if current_day % 3 == 0:
        points += points_tree_skirt
        total_price += price_tree_skirt * decorations_quantity

        points += points_tree_garland
        total_price += price_tree_garland * decorations_quantity

    if current_day % 5 == 0:
        points += points_tree_lights
        total_price += price_tree_lights * decorations_quantity

    if current_day % 5 == 0 and current_day % 3 == 0:
        points += 30

    if current_day % 10 == 0:
        points -= 20
        total_price += price_tree_skirt + price_tree_garland + price_tree_lights
        if current_day == days_left:
            points -= 30

print(f"Total cost: {total_price}")
print(f"Total spirit: {points}")



