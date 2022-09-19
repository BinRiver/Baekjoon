n = int(input())
a = list(map(int, input().split()))
m = max(a)
result = 0
for i in range(0, n):
    a[i] = a[i]/m * 100
    result += a[i]
print(result/n)