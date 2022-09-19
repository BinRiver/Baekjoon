num_dict = {}
for i in range(1, 10):
    n = int(input())
    num_dict[n] = i
print(max(num_dict))
print(num_dict[max(num_dict)])