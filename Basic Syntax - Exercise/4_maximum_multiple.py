divisor = int(input())
boundary = int(input())

for index in range(boundary, 0, -1):
    if index % divisor == 0:
        print(index)
        break
