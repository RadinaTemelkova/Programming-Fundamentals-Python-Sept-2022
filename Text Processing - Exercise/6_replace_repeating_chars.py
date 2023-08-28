some_string = input()
new_string = ""
previous_letter = ""

for letter in some_string:
    if letter == previous_letter:
        continue
    else:
        new_string += letter

    previous_letter = letter

print(new_string)




