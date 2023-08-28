command = input()

while command != "End":

    if command == "SoftUni":
        command = input()
        continue
    for symbol in command:
        for index in range(2):
            print(symbol, end="")
    print()
    command = input()
