def is_palindrome(p):
    t = str(p)
    t = reversed(t)
    if p == int(t):
        return True
    return False
