number_of_letters = int(input())
for first_index in range(97, 97 + number_of_letters):
    for second_index in range(97, 97 + number_of_letters):
        for third_index in range(97, 97 + number_of_letters):
            print(chr(first_index), end="")
            print(chr(second_index), end="")
            print(chr(third_index))




