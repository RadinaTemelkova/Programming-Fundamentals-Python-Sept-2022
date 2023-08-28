factor_number = int(input())
count_numbers = int(input())
list_of_multiples = []
for index in range(1, count_numbers+1):
    current_number = factor_number * index
    list_of_multiples.append(current_number)
print(list_of_multiples)
