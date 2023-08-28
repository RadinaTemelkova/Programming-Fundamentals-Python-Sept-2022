phonebook = {}
while True:
    command = input().split("-")
    if len(command) < 2:
        break
    name = command[0]
    number = command[1]
    phonebook[name] = number

counter = int("".join(command))
for index in range(counter):
    searched_contact = input()
    if searched_contact in phonebook.keys():
        print(f"{searched_contact} -> {phonebook[searched_contact]}")
    else:
        print(f"Contact {searched_contact} does not exist.")
