sequence_of_numbers = input().split()
numbers_list = list(map(int, sequence_of_numbers))
result = filter(lambda x: x % 2 == 0, numbers_list)
print(list(result))

