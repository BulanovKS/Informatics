A = ['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y', 1, 8, 'E', 'J', 'S', 'Z']
B = ['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y', 1, 8, 3, 'L', '2', '5']

print("Enter string: ")
C = input()
c = 0
t = 0
for k in range(len(C)):
    for i in range(len(A)):
        if (C[k] == A[i]) & (C[-k-1] == A[i]):
            c += 1
        elif (C[k] == A[i]) & (C[-k - 1] == B[i]):
            t += 1
if c == len(A): print(C, ' is a regular palindrome')
elif t == len(A): print(C, ' is a mirror palindrome')