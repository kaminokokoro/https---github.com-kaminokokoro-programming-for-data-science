n = int(input())
result = n
temp = str(n)
for i in range(1, n - 1):
    temp += str(n)
    result += int(temp)
print(result)
