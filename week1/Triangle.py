a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2
    print("S = ", (p * (p - a) * (p - b) * (p - c)) ** 0.5, " C = ", a + b + c)
