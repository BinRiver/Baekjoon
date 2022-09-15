r_list = []
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    r_list.append(a+b)
for i in range(0, len(r_list)):
    print(r_list[i])