list_of_strings = input().split()
number = 0
result = 0
final_results_list = []
for string in list_of_strings:
    first_letter = string[0]
    last_letter = string[-1]
    number = string.strip(first_letter)
    number = number.strip(last_letter)
    number = int(number)

    if first_letter.isupper():
        letter_position = ord(first_letter) - 64
        result = number / letter_position
    elif first_letter.islower():
        letter_position = ord(first_letter) - 96
        result = number * letter_position

    if last_letter.isupper():
        letter_position = ord(last_letter) - 64
        result -= letter_position
    elif last_letter.islower():
        letter_position = ord(last_letter) - 96
        result += letter_position

    final_results_list.append(result)
final_result = sum(final_results_list)
print(f"{final_result:.2f}")





