usernames_list = input().split(", ")
username_is_valid = False
valid_usernames = []
for username in usernames_list:
    if 3 <= len(username) <= 16:
        for symbol in username:
            if not(symbol.isalnum() or symbol == '-' or symbol == '_') or symbol == ' ':
                break
        else:
            username_is_valid = True
            valid_usernames.append(username)
print("\n".join(valid_usernames))


