S = input().upper()
num = []

for i in range(ord("A"), ord("Z")+1):
    num.append(S.count(chr(i)))

if num.count(max(num)) > 1:
    print("?")
else:
    print(chr(num.index(max(num))+65))