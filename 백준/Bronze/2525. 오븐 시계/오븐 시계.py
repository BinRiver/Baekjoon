A, B = map(int, input().split())
C = int(input())

all = A * 60 + B + C

if all >= 1440:
    all -= 1440
print(all//60, all%60)

    