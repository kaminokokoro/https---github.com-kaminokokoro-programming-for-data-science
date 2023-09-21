n = int(input())


def isPrime(n):
    if n == 2:
        return True
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def isSuperPrime(n):
    if isPrime(n):
        while n > 0:
            if not isPrime(n):
                return False
            n //= 10
        return True
    return False


if isSuperPrime(n):
    print("True")
else:
    print("False")
