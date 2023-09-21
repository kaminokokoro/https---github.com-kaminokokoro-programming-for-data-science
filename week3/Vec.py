import math


def cosineb2v(u, v):
    a = 0
    for i in range(len(u)):
        a += u[i] * v[i]
    b = 0
    for i in range(len(u)):
        b += u[i] ** 2
    c = 0
    for i in range(len(v)):
        c += v[i] ** 2
    d = math.sqrt(b) * math.sqrt(c)
    return a / d
