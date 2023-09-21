import math


def mean(s):
    return sum(s) / len(s)


def variance(s):
    means = mean(s)
    result = 0
    for i in s:
        result += (i - means) ** 2
    return result / len(s)


def standarddeviation(s):
    return math.sqrt(variance(s))
