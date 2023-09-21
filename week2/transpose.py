def inputMatrix():
    m = []
    while True:
        s = input()
        if s == "":
            break
        row = [int(i) for i in s.split()]
        m.append(row)
    return m


def transpose(m):
    t = []
    for i in range(0, len(m[0])):
        t.append([])
        for j in range(0, len(m)):
            t[i].append(m[j][i])
    return t


def printMatrix(m):
    # your code
    for i in range(0, len(m)):
        for j in range(0, len(m[i])):
            if j != len(m[i]) - 1:
                print(m[i][j], end=" ")
            else:
                print(m[i][j], end="")
        if i != len(m) - 1:
            print()


m = inputMatrix()
t = transpose(m)
printMatrix(t)
