import re

some_string = input()
while some_string:
    pattern = r"(\d+)"
    result = re.findall(pattern, some_string)
    if result:
        print(' '.join(result), end=" ")
    some_string = input()
