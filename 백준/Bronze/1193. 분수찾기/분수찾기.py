n = int(input())
k = 1

for i in range(1, n):
    if n > i:
        n -= i
        k += 1
    else:
        break
        
if k % 2 == 0:
    l = n
    r = k-n+1
else:
    l = k-n+1
    r = n

print("{}/{}".format(l,r))
