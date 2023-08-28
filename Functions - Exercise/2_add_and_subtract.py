def sum_numbers(number1, number2):
    return number1 + number2


def subtract(sum_of_two_numbers, number3):
    return sum_of_two_numbers - number3


def add_and_subtract(number1, number2, number3):
    sum_first_second_numbers = sum_numbers(number1, number2)
    final_result = subtract(sum_first_second_numbers, number3)
    return final_result


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))
