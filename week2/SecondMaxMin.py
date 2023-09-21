def input_array():
    array = []
    n = input().split(" ")
    for i in range(1, len(n)):
        array.append(int(n[i]))
    return array


def find_second_max_min(array):
    ar = list.copy(array)
    ar.sort()
    return ar[1], ar[-2]


array = input_array()
print(find_second_max_min(array))
