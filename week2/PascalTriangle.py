n = int(input())


def pascalTriangle(n):
    if n == 0:
        return [1]
    result = [[1], [1, 1]]
    for i in range(2, n + 1):
        result.append([])
        for j in range(0, i + 1):
            if j == 0 or j == i:
                result[i].append(1)
            else:
                result[i].append(result[i - 1][j - 1] + result[i - 1][j])
    return result


result = pascalTriangle(n)

for i in range(0, len(result)):
    for j in range(0, len(result[i])):
        print(result[i][j], end=" ")
    print()
