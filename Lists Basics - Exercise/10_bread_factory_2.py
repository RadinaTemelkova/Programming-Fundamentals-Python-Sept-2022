working_day_events = input().split("|")
energy = 100
coins = 100
factory_is_closed = False
ingredient = ''

for current_event in working_day_events:
    event = current_event.split("-")
    event_type = event[0]
    event_value = int(event[1])
    if "rest" == event_type:
        energy_for_gaining = event_value
        current_energy = energy
        energy += energy_for_gaining
        if energy > 100:
            energy = 100
            gained_energy = energy - current_energy
            print(f"You gained {gained_energy} energy.")
        else:
            print(f"You gained {energy_for_gaining} energy.")

        print(f"Current energy: {energy}.")

    elif "order" == event_type:
        earned_coins = event_value
        if energy >= 30:
            energy -= 30
            coins += earned_coins
            print(f"You earned {earned_coins} coins.")
        else:
            energy += 50
            print("You had to rest!")
            continue
    else:
        ingredient = event_type
        ingredient_price = event_value
        if ingredient_price <= coins:
            coins -= ingredient_price
            print(f"You bought {ingredient}.")
        else:
            factory_is_closed = True
            break

if factory_is_closed:
    print(f"Closed! Cannot afford {ingredient}.")
else:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")



