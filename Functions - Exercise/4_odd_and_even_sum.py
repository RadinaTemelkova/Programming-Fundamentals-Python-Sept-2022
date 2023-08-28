def sum_of_digits(current_number):
    current_number_as_string = str(current_number)
    even_sum = 0
    odd_sum = 0
    for digit in current_number_as_string:
        current_digit_as_int = int(digit)
        if current_digit_as_int % 2 != 0:
            odd_sum += current_digit_as_int
        else:
            even_sum += current_digit_as_int
    return [odd_sum, even_sum]


number = int(input())
result = sum_of_digits(number)
print(f"Odd sum = {result[0]}, Even sum = {result[1]}")

