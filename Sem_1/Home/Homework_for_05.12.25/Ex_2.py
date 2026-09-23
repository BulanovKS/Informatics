import numpy as np

def MNK (X, Y):
    X = np.array(X)
    Y = np.array(Y)
    mean_XY = np.mean(X * Y)
    mean_X = np.mean(X)
    mean_Y = np.mean(Y)
    mean_X_2 = np.mean(X ** 2)

    b = (mean_XY - mean_X * mean_Y) / (mean_X_2 - mean_X ** 2)
    a = mean_Y - b * mean_X
    a = round(a, 2)
    b = round(b, 2)
    return f"{float(a)}, {float(b)}"

