first_string, second_string = input().split()
longer_string = ''
shorter_string = ''
total_sum = 0
if len(first_string) == len(second_string):
    number_of_iterations = len(first_string)

else:
    if len(first_string) > len(second_string):
        longer_string = first_string
        shorter_string = second_string
    else:
        longer_string = second_string
        shorter_string = first_string

    number_of_iterations = len(shorter_string)

    for index in range(number_of_iterations, len(longer_string)):
        total_sum += ord(longer_string[index])

for index in range(number_of_iterations):
    result = ord(first_string[index]) * ord(second_string[index])
    total_sum += result

print(total_sum)
