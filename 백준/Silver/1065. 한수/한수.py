def han(i):
    num_list = []
    num_list = ' '.join(str(i)).split(' ')
    if len(num_list) <= 2:
        k = 1
    else:
        for j in range(1, len(num_list)-1):
            a = (int(num_list[j-1]) + int(num_list[j+1]))/2
            if a == int(num_list[j]):
                k = 1
                continue
            else:
                k = 0
                break
    if k == 1:
        return i
i = 0
n = int(input())
for m in range(1, n+1):
    if han(m) == m:
        i += 1
print(i)
