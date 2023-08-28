items = {"shards": 0, "fragments": 0, "motes": 0}
legendary_item = False
while True:
    materials_list = input().split()
    for x in range(0, len(materials_list), 2):
        current_quantity = int(materials_list[x])
        current_material = materials_list[x+1].lower()
        if current_material not in items.keys():
            items[current_material] = 0
        items[current_material] += current_quantity
        if items["shards"] >= 250:
            legendary_item = True
            items["shards"] -= 250
            print(f"Shadowmourne obtained!")
        elif items["fragments"] >= 250:
            legendary_item = True
            items["fragments"] -= 250
            print(f"Valanyr obtained!")
        elif items["motes"] >= 250:
            legendary_item = True
            items["motes"]-= 250
            print(f"Dragonwrath obtained!")
        if legendary_item:
            break
    if legendary_item:
        break
for key, value in items.items():
    print(f"{key}: {value}")









