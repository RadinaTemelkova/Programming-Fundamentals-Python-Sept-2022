unoccupied_electrons = int(input())
shells_list = []
shells_counter = 0

while unoccupied_electrons > 0:
    shells_counter += 1
    max_electrons_in_shell = 2 * shells_counter ** 2
    if unoccupied_electrons >= max_electrons_in_shell:
        shells_list.append(max_electrons_in_shell)
        unoccupied_electrons -= max_electrons_in_shell
    else:
        shells_list.append(unoccupied_electrons)
        unoccupied_electrons = 0

print(shells_list)




