n = input()
i = 0
nk = n


while True:
    if 0 <= int(nk) <= 9:
        n1 = '0' + nk
    else:
        n1 = nk
    a = int(n1[0])
    b = int(n1[1])
    nt = str(10*b + (a+b)%10)
    if nt == n:
        i += 1
        break
    else:
        nk = nt
        i += 1
        continue
print(i)