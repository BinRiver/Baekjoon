s = input()
for i in range(97, 123):
    if chr(i) in s:
        j = 0
        while True:
            if s[j] == chr(i):
                break
            else:
                j += 1
                continue
        print(j, end=' ')
    else:
        print(-1, end=' ')