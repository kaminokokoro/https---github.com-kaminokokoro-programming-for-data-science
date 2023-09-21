def inputMatrix():
    m = []
    while True:
        s = input()
        if s == "":
            break
        row = [int(i) for i in s.split()]
        m.append(row)
    return m


def isUpperTriangleMatrix(m):
    for i in range(0, len(m)):
        for j in range(0, len(m[i])):
            if i > j and m[i][j] != 0:
                return False
    return True


m = inputMatrix()
print(isUpperTriangleMatrix(m))
