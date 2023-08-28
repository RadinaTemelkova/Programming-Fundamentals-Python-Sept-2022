force_book = {}
user_is_force_user = False
while True:
    information = input()
    if information == "Lumpawaroo":
        break

    if "|" in information:
        force_side, force_user = information.split(" | ")

        for value in force_book.values():
            if force_user in value:
                user_is_force_user = True
                break

        if not user_is_force_user:
            if force_side not in force_book.keys():
                force_book[force_side] = [force_user]
            else:
                force_book[force_side].append(force_user)

    elif "->" in information:
        force_user, force_side = information.split(" -> ")

        for key, value in force_book.items():
            if force_user in value:
                user_is_force_user = True
                force_book[key].remove(force_user)
                force_book[force_side].append(force_user)
                break

        if not user_is_force_user:
            if force_side not in force_book.keys():
                force_book[force_side] = [force_user]
            else:
                force_book[force_side].append(force_user)

        print(f"{force_user} joins the {force_side} side!")

for key, value in force_book.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        for every_user in value:
            print(f"! {every_user}")














