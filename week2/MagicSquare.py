def isMagicSquare(m):
    sumcross1 = 0
    sumcross2 = 0
    for i in range(len(m)):
        sumCol = 0
        for j in range(len(m[i])):
            sumCol += m[j][i]
            if i == j:
                sumcross1 += m[i][j]
            if i + j == len(m[i]) - 1:
                sumcross2 += m[i][j]
        if sumCol != sum(m[i]) != sum(m[i - 1]):
            return False
    if sumcross1 != sumcross2 != sum(m[0]):
        return False
    return True


def inputMatrix():
    m = []
    while True:
        s = input()
        if s == "":
            break
        row = [int(i) for i in s.split()]
        m.append(row)
    return m
