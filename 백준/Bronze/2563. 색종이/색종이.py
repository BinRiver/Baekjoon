Paper = []

for i in range(100):
    Paper.append([0]*100)
    
Num = int(input())

for i in range(Num):
    M, N = map(int, input().split())
    for n in range(90-N, 100-N):
        for m in range(M, 10+M):
            Paper[n][m] = 1

area = 0
for i in range(100):
    area += Paper[i].count(1)

print(area)