def office_chairs(rooms):
    free_chairs = 0
    chairs_needed_list = []
    game_on = True

    for room in range(1, rooms + 1):
        chairs, visitors = input().split()

        if len(chairs) < int(visitors):
            game_on = False
            chairs_needed = int(visitors) - len(chairs)
            chairs_needed_list.append(f"{chairs_needed} more chairs needed in room {room}")
        else:
            free_chairs += len(chairs) - int(visitors)

    if game_on:
        return f"Game On, {free_chairs} free chairs left"
    else:
        return "\n".join(chairs_needed_list)


number_of_rooms = int(input())
print(office_chairs(number_of_rooms))

