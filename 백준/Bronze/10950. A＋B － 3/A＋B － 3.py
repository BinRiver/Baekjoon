t = int(input())
k = []
for i in range(1, t+1):
    a, b = map(int, input().split())
    k.append(a+b)
for j in range(0, t):
    print(k[j])
    