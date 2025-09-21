s = input()
k = [s[-1]] + [s[i] for i in range(len(s)-1)]
print(''.join(k)) # print() считается за третью строку?