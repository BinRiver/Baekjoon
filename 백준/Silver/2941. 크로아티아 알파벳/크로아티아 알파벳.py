word = input()

count = len(word)
for i in range(len(word)):
    if word[i] == '=':
        if word[i-1] == 'c' or word[i-1] == 's':
            count -= 1
        else:
            if word[i-2] == 'd':
                count -= 2
            else:
                count -= 1
    elif word[i] == '-':
        count -= 1
    elif word[i] == 'j':
        if word[i-1] == 'l' or word[i-1] == 'n':
            count -= 1
    else:
        continue
print(count)