N = int(input())

a, b, c = 1, 2, 1

if N == 1:
    print(1)
while N not in range(a, b):
    a = b
    b = b + 6 * c
    if N in range(a, b):
        print(c+1)
    else:
        c += 1