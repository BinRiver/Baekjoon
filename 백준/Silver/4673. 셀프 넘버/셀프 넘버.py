def d(n):
    result = 0
    result += n
    num_list = []
    num_list = ' '.join(str(n)).split(' ')
    for i in range(0, len(num_list)):
        result += int(num_list[i])
    return result

i = 1
result_list = []
while i < 10000:
    result_list.append(d(i))
    i += 1
result_list.sort()
result_list = set(result_list)

for i in range(1, 10000):
    if i not in result_list:
        print(i)
