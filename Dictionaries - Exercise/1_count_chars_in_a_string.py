some_string = input()
occurrences = {}

for character in some_string:
    if character != " ":
        if character not in occurrences.keys():
            occurrences[character] = 0
        occurrences[character] += 1
for key, value in occurrences.items():
    print(f"{key} -> {value}")


