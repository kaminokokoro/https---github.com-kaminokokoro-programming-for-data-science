# Hoàn thiện hàm customSort

import functools


def compare(a, b):
    if a % 2 == 0 and b % 2 == 1:
        return -1
    if a % 2 == 1 and b % 2 == 0:
        return 1
    if a % 2 == 0 and b % 2 == 0:
        return a - b
    if a % 2 == 1 and b % 2 == 1:
        return b - a


def customSort(a):
    """
    Hàm thực hiện sắp xếp các phần tử trong a, theo thứ tự:
    - Chẵn bên trái, lẻ bên phải
    - Chẵn tăng dần, lẻ giảm dần
    ví dụ a  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    kết quả là [2, 4, 6, 8, 10, 9, 7, 5, 3, 1]
    """
    list.sort(a, key=functools.cmp_to_key(compare))
    return a
