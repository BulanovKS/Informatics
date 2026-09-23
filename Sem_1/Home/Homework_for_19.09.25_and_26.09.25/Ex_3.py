s = str(input())
A = [0] * len(s)
B = [0] * len(s)
for i in range(0, len(s)):
    A[i] = s[i]
    B[i] = s[-i-1]

C = ['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y', '1', '8']

mirpal, regpal, mirstr = 0, 0, 0

for i in range(0, len(s)):
    if A[i] == B[i] and A[i] in C:
        mirpal += 1
    elif (A[i] == 'E' and B[i] == '3') or (A[i] == '3' and B[i] == 'E') or (A[i] == 'J' and B[i] == 'L') or (A[i] == 'L' and B[i] == 'J') or (A[i] == 'S' and B[i] == '2') or (A[i] == '2' and B[i] == 'S') or (A[i] == 'Z' and B[i] == '5') or (A[i] == '5' and B[i] == 'Z'):
        mirstr += 1
    elif A[i] == B[i]:
        regpal += 1

if mirpal == len(s): print(s, " is a mirrored palindrome")
elif mirpal + regpal == len(s): print(s, " is a regular palindrome")
elif mirpal + regpal + mirstr == len(s): print(s, " is a mirrored string")
else: print(s, " is not a palindrome")