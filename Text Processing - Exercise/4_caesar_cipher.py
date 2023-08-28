some_text = input()
for character in some_text:
    encrypted_character = chr(ord(character) + 3)
    print(encrypted_character, end="")

