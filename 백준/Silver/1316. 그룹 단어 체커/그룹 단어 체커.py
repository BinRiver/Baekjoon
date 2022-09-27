N = int(input())
count = 0

for i in range(N):
    S = list(input())
    S2 = list(set(S))
    for j in S2:
        Index = list(filter(lambda x: S[x] == j, range(len(S))))
        num = Index[0]
        for k in range(len(Index)):
            Index[k] -= num
            if k != Index[k]:
                count -= 1
                loop = False
                break
            else:
                loop = True
        if loop == False:
            count += 1
            break
    if loop == True:
        count += 1

print(count)