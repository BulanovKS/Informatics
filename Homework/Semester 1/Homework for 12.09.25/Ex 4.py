a = open('input.txt', 'r')
line = a.readline()
A = list(map(float, line.split()))
line = a.readline()
b = 0
c = 1
if line == '+':
    for i in range(len(A)):
        b += A[i]
elif line == '-':
    for i in range(len(A)):
        b -= A[i]
elif line == '*':
    for i in range(len(A)):
        c *= A[i]
a.close()
d = open('output.txt', 'w')
d.write(str(b) + " - or result of summation" + '\n')
d.write(str(c) + " - or result of multiplication" + '\n')
d.close()