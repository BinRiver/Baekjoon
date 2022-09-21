n = int(input())
result_list = []
for i in range(n):
    num, s = input().split()
    num = int(num)
    k = ''
    for j in range(len(s)):
        result = s[j]*num
        k += result
    result_list.append(k)
for i in range(len(result_list)):
    print(result_list[i])