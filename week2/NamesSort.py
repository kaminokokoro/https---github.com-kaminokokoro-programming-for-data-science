# -*- coding: utf-8 -*-

import locale
import functools

locale.setlocale(locale.LC_ALL, "vi_VN")


def inputList():
    names = []
    while True:
        name = input()
        if name == "":
            break
        name += ""
        names.append(name)
    return names


def getName(s):
    fullname = s.split(" ")
    lname = fullname[-1]
    fname = " ".join(fullname[:-1])
    return (lname, fname)


def sortNamesList(names):
    list.sort(names, key=functools.cmp_to_key(compareNames))
    return names


def compareNames(name1, name2):
    if getName(name1)[0] != getName(name2)[0]:
        return 1 if getName(name1)[0] > getName(name2)[0] else -1
    return 1 if getName(name1)[1] >= getName(name2)[1] else -1


inputList = inputList()
sortNamesList = sortNamesList(inputList)
for name in sortNamesList:
    print(name)
    print(type(name))
