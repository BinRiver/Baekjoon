N = int(input())
S = input()
se = S.count("y")
big = N - se
if se > big:
    print("security!")
elif se < big:
    print("bigdata?")
else:
    print("bigdata? security!")