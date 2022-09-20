def Han(n):
    if n < 100:
        return 1
    else:
        num = list(map(int, str(n)))
        d = num[1] - num[0]
        k = 0
        for i in range(0, len(num)):
            for j in range(k, len(num)):
                num[j] -= d
            k += 1
        num = list(set(num))
        if len(num) == 1:
            return 1
        else:
            return 0

N = int(input())
count = 0
for i in range(1, N+1):
    count += Han(i)
print(count)
