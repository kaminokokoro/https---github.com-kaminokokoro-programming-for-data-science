def slover(a, b, c):
    if a == 0 and b == 0 and c == 0:
        print("VSN")
        return
    if a == 0:
        print(-c / b)
        return
    delta = float(b**2 - 4 * a * c)
    if delta < 0:
        print("VN")
    elif delta == 0:
        print(-b / (2 * a))
    else:
        print((-b - delta**0.5) / (2 * a), (-b + delta**0.5) / (2 * a))
