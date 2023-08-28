number_of_lines = int(input())
capacity = 255
sum_litres = 0
for current_line in range (number_of_lines):
    current_litres = int(input())
    sum_litres += current_litres
    if sum_litres > capacity:
        print("Insufficient capacity!")
        sum_litres -= current_litres
print(sum_litres)


