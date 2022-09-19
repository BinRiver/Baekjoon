N = int(input())

for i in range(N):
    OX = list(input())
    index = 0
    count = 0
    sum = 0
    while index < len(OX):
        if OX[index] == "O":
            count += 1
        else:
            count = 0
        index += 1
        sum += count
    print(sum)
