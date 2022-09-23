S = input()

c = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in c:
    if i in S:
        S = S.replace(i, "*")
print(len(S))
