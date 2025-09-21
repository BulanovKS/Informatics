A = []
a = 1
for i in range(int(input())):
    A.append(int(input()))
    print(A[i])
for j in range(len(A)):
    a *= A[j]
b = a ** (1/len(A))
print(b)