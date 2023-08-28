numbers_string = input()
numbers_list = numbers_string.split()
opposite_numbers_list = []
for symbol in numbers_list:
    current_number = int(symbol)
    if current_number > 0:
        opposite_number = current_number - 2*current_number
    else:
        opposite_number = abs(current_number)
    opposite_numbers_list.append(opposite_number)
print(opposite_numbers_list)

