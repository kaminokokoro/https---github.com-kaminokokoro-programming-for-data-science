# giải phương trình f(x) = 0, tìm nghiệm xấp xỉ c theo phương pháp chia đôi.
import math


# giải phương trình f(x) = 0, tìm nghiệm xấp xỉ c theo phương pháp chia đôi.
# giải phương trình f(x) = 0, tìm nghiệm xấp xỉ c theo phương pháp chia đôi.
def solver(f, a, b, e=0.000001):
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b
    if f(a) * f(b) > 0:
        return None
    c = (a + b) / 2
    while abs(f(c)) >= e:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c
