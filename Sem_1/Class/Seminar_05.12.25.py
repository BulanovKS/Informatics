def replacements(stroke, i, j, k):
    alphabet = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0}
    for keys in alphabet.keys():
        alphabet[keys] = stroke[i-1:j].count(keys)
    if k == 1:
        for t in range(i-1, j):
            for keys in alphabet.keys():
                if alphabet[keys] != 0:
                    stroke[t] = keys
                    alphabet[keys] -= 1
                    break
    elif k == 0:
        for s in range(i-1, j):
            for keys in reversed(alphabet.keys()):
                if alphabet[keys] != 0:
                    stroke[s] = keys
                    alphabet[keys] -= 1
                    break

    return stroke

n, q = map(int, input().split())
S = input()
Stroke = [i for i in S]
for t in range(q):
    i_, j_, k_ = map(int, input().split())
    Stroke = replacements(Stroke, i_, j_, k_)

print("".join(Stroke))