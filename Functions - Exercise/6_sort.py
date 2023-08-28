sequence_of_numbers = input().split()
numbers_list = list(map(int, sequence_of_numbers))
result = sorted(numbers_list)
print(list(result))
