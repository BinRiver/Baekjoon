A = []
for i in range(9):
    A.append(list(map(int, input().split())))

max_list = list(map(max, A))

N = max_list.index(max(max_list))
M = A[N].index(max(max_list))

print(A[N][M])
print(N+1, M+1, sep = " ")