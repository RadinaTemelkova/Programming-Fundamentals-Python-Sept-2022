number_of_snowballs = int(input())
greatest_snowball_value = 0
greatest_snowball_weight = 0
greatest_snowball_time = 0
greatest_snowball_quality = 0

for current_snowball in range(number_of_snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    current_snowball_value = int(snowball_weight/snowball_time) ** snowball_quality
    if current_snowball_value >= greatest_snowball_value:
        greatest_snowball_value = current_snowball_value
        greatest_snowball_weight = snowball_weight
        greatest_snowball_time = snowball_time
        greatest_snowball_quality = snowball_quality

print(f"{greatest_snowball_weight} : {greatest_snowball_time} = {greatest_snowball_value} ({greatest_snowball_quality})")
