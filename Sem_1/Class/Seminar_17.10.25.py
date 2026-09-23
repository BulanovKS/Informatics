#Task A

"""
N, M = map(int, input().split())
X = [0] + list(map(int, input().split()))
Y = [0] + list(map(int, input().split()))

dp = [[0] * (M + 1) for i in range(N + 1)]

for i in range(0, N + 1):
    for j in range(0, M + 1):

        dp[0][j] = 0
        dp[i][0] = 0
        dp[i][j] = dp[i-1][j]

        if (j >= X[i]) and (dp[i-1][j-X[i]] + Y[i] > dp[i][j]):
            dp[i][j] = dp[i-1][j-X[i]] + Y[i]
print(dp[N][M])
"""

#Task D

"""
N, M = map(int, input().split())

def f(N, M):
    if (N % 2 ==0) or (M % 2 == 0): return 0
    else: return 1 + 4 * f(N//2, M//2)

print(f(N, M))
"""

# Task F

"""
i ^ j = k | ^i

i ^ j ^ i = k ^ i

i ^ i = 0, j ^ 0 = j

j = k ^ i

n, k = map(int, input().split())
A = list(map(int, input().split()))

def f(n, k , A):
    M = 0
    for i in range(2 ** n):
        if A[i] + A[k ^ i] > M: M = A[i] + A[k ^ i]
    return M

print(f(n, k, A))
"""

# Task B

"""
a, b = map(int, input().split())

def find_x(a,b):
    x = 0
    while not(((a + x) % b == 0) and ((b + x) % a == 0)):
        x += 1
    return x

print(find_x(a, b))
"""

# Task F

"""
n, m = map(int, input().split())

C = [[-1001] * (m + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    A = list(map(int, input().split()))
    for j in range(1, m + 1):
        C[i][j] = A[j - 1]

dp = [[[-1001] * 3 for i in range(m + 1)] for j in range(n + 1)]

for k in range(0, 3):
   dp[1][1][k] = C[1][1]

for i in range(1, n + 1):
    for j in range(1, m + 1):
            if i>=2:
                dp[i][j][0] = max(dp[i - 1][j][1], dp[i - 1][j][2]) + C[i][j]
            if j>=2:
                dp[i][j][1] = max(dp[i][j - 1][0], dp[i][j - 1][2]) + C[i][j]
            if (i>=2) and (j>=2):
                dp[i][j][2] = max(dp[i - 1][j - 1][0], dp[i - 1][j - 1][1]) + C[i][j]
print(max(dp[n][m]))
"""

# Task C

"""
n = int(input())
dp = [[0] * (n + 1) for i in range(n + 1)]
dp[0][0] = 1
for i in range(1, n + 1):
        for j in range(0, i):

        for j in range(i, n + 1):
            dp[i][j] = dp[i - 1][j]
    return dp[n][n]
"""