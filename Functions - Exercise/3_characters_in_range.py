def in_between_characters(first, second):
    for current_value in range(ord(first) + 1, ord(second)):
        current_symbol = chr(current_value)
        print(current_symbol, end=" ")


character1 = input()
character2 = input()
in_between_characters(character1, character2)

