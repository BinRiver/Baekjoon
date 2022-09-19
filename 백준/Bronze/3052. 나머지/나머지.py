n_list = []
r_list = []
for i in range(0, 10):
    n = int(input())
    n_list.append(n)
    r_list.append(n_list[i]%42)
r_list = list(set(r_list))
print(len(r_list))