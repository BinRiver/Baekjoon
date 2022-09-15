clo, min = input().split(" ")

if 45 <= int(min) <= 59:
    upclo = int(clo)
    upmin = int(min) - 45
else:
    if int(clo) > 0:
        upclo = int(clo)-1
        upmin = 60 -(45-int(min))
    else:
        upclo = 23
        upmin = 60 -(45-int(min))

print("{} {}".format(upclo, upmin))
