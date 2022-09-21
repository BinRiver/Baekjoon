S = list(input())
C = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
time = 0
for i in S:
    for j in range(len(C)):
        if i in C[j]:
            time += (j+3)
        
print(time)
