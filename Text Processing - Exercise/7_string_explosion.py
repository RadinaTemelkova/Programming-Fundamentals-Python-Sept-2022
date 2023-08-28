some_string = input()
result = ""
strength = 0
for index, element in enumerate(some_string):
    if element == ">":
        result += element
        strength += int(some_string[index + 1])
    elif strength > 0 and element != ">":
        strength -= 1
    else:
        result += element
print(result)
