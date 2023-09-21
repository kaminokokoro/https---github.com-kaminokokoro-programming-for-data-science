def inputArray():
    array = []
    n = input().split(" ")
    for i in range(1, len(n)):
        array.append(int(n[i]))

    return array


def sort_array(array):
    r = list.copy(array)
    r.sort()
    return r


def printArray(r):
    for i in range(0, len(r)):
        print(r[i], end=" ")


arr = inputArray()
r = sort_array(arr)
printArray(r)
