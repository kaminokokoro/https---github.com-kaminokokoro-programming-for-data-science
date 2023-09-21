n = int(input())


def dualFactorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * dualFactorial(n - 2)


print(str(n) + "!! =", dualFactorial(n))
