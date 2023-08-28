messages_counter = int(input())
for x in range(messages_counter):
    current_number = int(input())
    if current_number == 88:
        print("Hello")
    elif current_number == 86:
        print("How are you?")
    elif current_number < 88:
        print("GREAT!")
    else:
        print("Bye.")
