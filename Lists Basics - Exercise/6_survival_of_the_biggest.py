import sys
min_number = sys.maxsize
min_number_index = 0
starting_list = input().split()
count_of_numbers_to_remove = int(input())
current_number = 0

for index in range(count_of_numbers_to_remove):
    min_number = sys.maxsize
    for current_index, current_number in enumerate(starting_list):
        current_number = int(current_number)
        if current_number < min_number:
            min_number = current_number
            min_number_index = current_index
    starting_list.pop(min_number_index)
print(", ".join(starting_list))





