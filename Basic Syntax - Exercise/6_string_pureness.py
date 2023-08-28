number = int(input())
string_is_pure = True
for index in range (number):
    current_string = input()
    for symbol in current_string:
        if symbol == "," or symbol == "." or symbol == "_":
            string_is_pure = False
            print(f"{current_string} is not pure!")
            break
    else:
        print(f"{current_string} is pure.")

