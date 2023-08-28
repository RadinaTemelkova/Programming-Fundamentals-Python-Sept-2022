first_sequence = input().split(", ")
second_sequence = input().split(", ")
result = []
for word_1 in first_sequence:
    for word_2 in second_sequence:
        if word_1 in word_2:
            result.append(word_1)
            break
print(result)
