a = input()
result = 0
for i in range(0, len(a)):
    if 'A' == a[i] or 'B' == a[i] or 'C' == a[i]:
        result += 3
    elif 'D' == a[i] or 'E' == a[i] or 'F' == a[i]:
        result += 4
    elif 'G' == a[i] or 'H' == a[i] or 'I' == a[i]:
        result += 5
    elif 'J' == a[i] or 'K' == a[i] or 'L' == a[i]:
        result += 6
    elif 'M' == a[i] or 'N' == a[i] or 'O' == a[i]:
        result += 7
    elif 'P' == a[i] or 'Q' == a[i] or 'R' == a[i] or 'S' == a[i]:
        result += 8
    elif 'T' == a[i] or 'U' == a[i] or 'V' == a[i]:
        result += 9
    else:
        result += 10
print(result)