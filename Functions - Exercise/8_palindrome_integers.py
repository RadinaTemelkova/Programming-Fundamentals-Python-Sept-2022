def palindrome_func(list_of_numbers):
    number_is_palindrome = False
    list_of_numbers_as_string = list(map(str, list_of_numbers))

    for number in list_of_numbers_as_string:
        if number == number[::-1]:
            number_is_palindrome = True
        else:
            number_is_palindrome = False
        print(number_is_palindrome)


sequence_of_numbers = list((input().split(", ")))
numbers = list(map(int, sequence_of_numbers))
palindrome_func(numbers)


