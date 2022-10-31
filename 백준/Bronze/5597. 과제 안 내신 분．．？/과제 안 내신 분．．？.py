n = list(range(1,31))

for i in range(28):
    n.remove(int(input()))

print(n[0], n[1], sep = "\n")