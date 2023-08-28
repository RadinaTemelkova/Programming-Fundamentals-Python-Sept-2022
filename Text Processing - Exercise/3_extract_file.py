path_string = input().split('\\')
result = path_string[len(path_string)-1].split('.')
print(f"File name: {result[0]}")
print(f"File extension: {result[1]}")

