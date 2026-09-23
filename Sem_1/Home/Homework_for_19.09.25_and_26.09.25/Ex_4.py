s = input()
k = [i for i in s]
for i in range(1, len(s), 2): k[i-1], k[i] = s[i], s[i-1]
print(''.join(k)) # print() считается за четвертую строку?