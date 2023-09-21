n = int(input())
for i in range(3, n + 1):
    for j in range(i, n + 1):
        temp = float((i**2 + j**2)) ** 0.5
        if temp.is_integer() and temp <= n:
            print(
                str("(") + str(i) + str(","),
                str(j) + str(","),
                str(int(temp)) + str(")"),
            )
