first_index = int(input())
last_index = int(input())

for current_index in range(first_index, last_index+1):
    print(chr(current_index), end=" ")
