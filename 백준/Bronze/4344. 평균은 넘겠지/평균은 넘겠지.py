test_num = int(input())
result_list = []

for i in range(0, test_num):
    num_list = list(map(int, input().split()))
    num = num_list[0]
    result = 0
    for l in range(1, num+1):
        result += num_list[l]
    avg = result / num
    k = 0
    for j in range(1, num+1):
        if num_list[j] > avg:
            k += 1
    result_list.append(k/num*100)
for i in range(0, len(result_list)):
    print('{0:0.3f}%'.format(result_list[i]))