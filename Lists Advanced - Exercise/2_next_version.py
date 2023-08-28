current_version = list(map(int, input().split(".")))

for index in range(len(current_version)-1, -1, -1):
    if current_version[index] + 1 <= 9:
        current_version[index] += 1
        break
    else:
        current_version[index] = 0
        if current_version[index-1] + 1 <= 9:
            current_version[index - 1] += 1
        else:
            current_version[index-1] = 0
            current_version[index - 2] += 1
        break
print(".".join(list(map(str, current_version))))



