sums = input().split(", ")
sums_in_int = []
count_of_beggars = int(input())
all_beggars_profit = []
beggar_starting_index = 0

for element in sums:
    sums_in_int.append(int(element))

while beggar_starting_index < count_of_beggars:
    current_beggar_profit = 0
    for current_index in range(beggar_starting_index, len(sums_in_int), count_of_beggars):
        current_beggar_profit += sums_in_int[current_index]
    all_beggars_profit.append(current_beggar_profit)
    beggar_starting_index += 1

print(all_beggars_profit)






