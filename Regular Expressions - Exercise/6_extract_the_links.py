import re

sentence = input()
pattern = r"\b(www\.([a-zA-Z0-9\-]+)(\.[a-z]+)+)\b"

while sentence:
    valid_links = re.findall(pattern, sentence)
    for link in valid_links:
        print(link[0])
    sentence = input()

