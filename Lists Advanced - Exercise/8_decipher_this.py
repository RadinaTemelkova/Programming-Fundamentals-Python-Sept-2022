secret_message = input().split()
deciphered_message = []

for word in secret_message:
    digits_list = list(filter(lambda symbol: symbol.isdigit(), word))
    first_letter_code = int(''.join(digits_list))
    first_letter = chr(first_letter_code)
    deciphered_message.append(first_letter)

    letters_list = list(filter(lambda symbol: symbol.isalpha(), word))
    letters_list[0], letters_list[-1] = letters_list[-1], letters_list[0]
    next_letters = ''.join(letters_list)
    deciphered_message.append(next_letters)
    deciphered_message.append(' ')
print(''.join(deciphered_message), end=" ")
