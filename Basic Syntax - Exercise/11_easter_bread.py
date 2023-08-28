budget = float(input())
price_per_kilo_flour = float(input())

price_per_pack_of_eggs = 0.75 * price_per_kilo_flour
milk_price_per_liter = 1.25 * price_per_kilo_flour
money_per_bread = price_per_kilo_flour + price_per_pack_of_eggs + milk_price_per_liter/4
difference = budget - money_per_bread
bread_counter = 1
colored_eggs_counter = 3
while difference >= money_per_bread:
    bread_counter += 1
    difference -= money_per_bread
    colored_eggs_counter += 3
    if bread_counter % 3 == 0:
        colored_eggs_counter = colored_eggs_counter - (bread_counter - 2)


print(f"You made {bread_counter} loaves of Easter bread! Now you have {colored_eggs_counter} eggs and {difference:.2f}BGN left.")