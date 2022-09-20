def d(n):
    for i in str(n):
        n += int(i)
    return n

numbers = set(range(1, 10001))
no_self_numbers = set()

for j in range(1, 10001):
    if d(j) <= 10000:
        no_self_numbers.add(d(j))
self_numbers = sorted(list(numbers - no_self_numbers))

for k in self_numbers:
    print(k)
