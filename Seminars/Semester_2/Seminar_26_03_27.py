#TODO Z- и ПРЕФИКС-ФУНКЦИИ

def z_function(s):
    n = len(s)
    zf = [0] * n
    left, right = 0, 0
    for i in range(1, n):
        zf[i] = max(0, min(right - i, zf[i - left]))
        while i + zf[i] < n and s[zf[i]] == s[i + zf[i]]:
            zf[i] += 1
        if i + zf[i] > right:
            left = i
            right = i + zf[i]
    return zf

def prefix_function(s):
    n = len(s)
    p = [0] * n
    for i in range(1, len(s)):
        k = p[i - 1]
        while k > 0 and s[k] != s[i]:
            k = p[k - 1]
        if s[k] == s[i]:
            k += 1
        p[i] = k
    return p