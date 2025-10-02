s = input()
m = 0
res = ''

for i in range(len(s)):
    t = 0
    for k in range(len(s)):
        if s[i] == s[k]:
            t += 1
    if m < t:
        m = t
        res = s[i]
print(res)