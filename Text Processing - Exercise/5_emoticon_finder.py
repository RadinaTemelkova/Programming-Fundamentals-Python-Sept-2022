some_text = input()
for index, character in enumerate(some_text):
    if character == ":":
        print(f":{some_text[index + 1]}")
