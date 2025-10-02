s = input()

for i in range(len(s)):
    t = 0
    for k in range(len(s)):
        if s[i] == s[k]:
            t += 1
    if t == 1: print(s[i])