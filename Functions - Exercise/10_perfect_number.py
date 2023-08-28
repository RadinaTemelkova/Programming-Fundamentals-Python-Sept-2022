def perfect_number_function(current_number):
    sum_of_divisors = 0
    for divisor in range(1, current_number):
        if current_number % divisor == 0:
            sum_of_divisors += divisor
    if current_number == sum_of_divisors:
        return "We have a perfect number!"

    return "It's not so perfect."


number = int(input())
result = perfect_number_function(number)
print(result)