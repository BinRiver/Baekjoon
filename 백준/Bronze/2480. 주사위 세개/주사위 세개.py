a, b, c = map(int, input().split())

if a != b and b != c and c != a:
    print(100*max(a,b,c))
elif a != b:
    if a == c or b == c:
        print(1000+c*100)
elif b != c:
    if a == b or a == c:
        print(1000+a*100)
elif c != a:
    if b == c or b == a:
        print(1000+b*100)
else:
    print(10000+a*1000)
        
        
    
        