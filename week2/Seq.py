def isAlt(a):
    for i in range(1, len(a)):
        if a[i] * a[i - 1] >= 0:
            return False
    return True


def isGrow(a):
    for i in range(1, len(a)):
        if a[i] - a[i - 1] < 0:
            return False
    return True


def isMulti(a):
    q = a[1] / a[0]
    for i in range(1, len(a)):
        if a[i] / a[i - 1] != q:
            return False
    return True


def isAdd(a):
    q = round(a[1] - a[0])

    for i in range(1, len(a)):
        if round(a[i] - a[i - 1]) != q:
            return False
    return True
