n = int(input())
result_list = []

for i in range(0, n):
    OX = input()
    OX_list = ' '.join(OX).split(' ')
    num = len(OX_list)
    k = 0
    result = 0
    for l in range(0, num):
        if OX_list[l] == 'O':
            k += 1
        else:
            k = 0
        if k > 0:
            result += k
    result_list.append(result)

for i in range(0, n):
    print(result_list[i])