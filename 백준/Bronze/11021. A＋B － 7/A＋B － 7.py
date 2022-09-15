t = int(input())

r_list = []
for i in range(0, t):
    a, b = map(int, input().split())
    r_list.append(a+b)
for k in range(0, t):
    print("Case #{}: {}".format(k+1, r_list[k]))