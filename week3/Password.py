def checkPassword(s):
    if len(s) < 8 or len(s) > 100:
        return False
    isUpper = False
    isDigit = False
    isSpecial = False
    for i in s:
        if i.isupper() == True:
            isUpper = True
        if i.isdigit() == True:
            isDigit = True
        if i in "~!@#$%^&*":
            isSpecial = True

    return isUpper and isDigit and isSpecial
