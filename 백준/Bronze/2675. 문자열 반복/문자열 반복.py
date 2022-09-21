T = int(input())

for i in range(T):
    N, S = input().split(" ")
    S = list(S)
    N = int(N)
    for j in S:
        print(j*N, end="")
    print()
