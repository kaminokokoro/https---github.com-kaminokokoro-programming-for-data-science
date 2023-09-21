def is_palindrome(p):
    t = str(p)
    t = reversed(t)
    if int(p) == int("".join(t)):
        return True
    return False
