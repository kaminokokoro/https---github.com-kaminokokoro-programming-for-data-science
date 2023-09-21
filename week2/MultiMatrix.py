import numpy as np


def inputMatrix():
    m = []
    n = input()
    for i in range(0, int(n[0])):
        s = input()
        row = []
        for j in s.split():
            if j.isdigit() == True:
                row.append(int(j))
        m.append(row)
    return m


def multiMatrix(m1, m2):
    array1 = np.array(m1)
    array2 = np.array(m2)
    result = np.dot(array1, array2)
    r = result.tolist()
    return r


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


n1 = input()
m1 = inputMatrix()
m2 = inputMatrix()

mm = multiMatrix(m1, m2)
printMatrix(mm)
