all_numbers = [int(numbers) for numbers in input().split(", ")]

positive_numbers = [str(number) for number in all_numbers if number >= 0]

print(f"Positive: {', '.join(positive_numbers)}")
negative_numbers = [str(number) for number in all_numbers if number < 0]

print(f"Negative: {', '.join(negative_numbers)}")
even_numbers = [str(number) for number in all_numbers if number % 2 == 0]

print(f"Even: {', '.join(even_numbers)}")
odd_numbers = [str(number) for number in all_numbers if number % 2 != 0]

print(f"Odd: {', '.join(odd_numbers)}")

