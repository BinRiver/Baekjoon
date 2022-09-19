C = int(input())

for i in range(C):
    N = list(map(int, input().split()))
    avg = 0
    for j in range(1, len(N)):
        avg += N[j]
    avg = avg/N[0]
    count = 0
    for num in range(1, len(N)):
        if N[num] > avg:
            count += 1
    print("{:.3f}%".format(count/N[0]*100))
