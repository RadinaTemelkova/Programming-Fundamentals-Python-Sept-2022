numbers = input().split(", ")
max_value = 0
numbers_list = [int(number) for number in numbers]

while numbers_list:
    max_value += 10
    group = list(filter(lambda x: x <= max_value, numbers_list))
    print(f"Group of {max_value}'s: {group}")

    for element in group:
        while element in numbers_list:
            numbers_list.remove(element)

