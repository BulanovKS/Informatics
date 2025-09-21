N = int(input()) # а зачем оно нужно?
s = list(map(int, input().split(' ')))

for i in range(len(s)):
    t = 0
    for k in range(len(s)):
        if s[i] > s[k]: t += 1
        elif s[i] < s[k]: t -= 1
    if t == 0: print(s[i])