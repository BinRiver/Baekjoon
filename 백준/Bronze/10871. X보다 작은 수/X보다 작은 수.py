n, x = map(int, input().split())
a = input().split(' ')

for i in range(0, n):
    if int(a[i]) < x:
        print(a[i], end = ' ')