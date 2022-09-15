t = int(input())

r_list = []
a_list = []
b_list = []
for i in range(0, t):
    a, b = map(int, input().split())
    r_list.append(a+b)
    a_list.append(a)
    b_list.append(b)
for k in range(0, t):
    print("Case #{}: {} + {} = {}".format(k+1, a_list[k], b_list[k], r_list[k]))