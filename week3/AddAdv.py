# Hoàn thiện hàm addNum(a, b) theo yêu cầu trong đề bài


def addNum(a, b):
    """
    Cho 2 số nguyên a, b được biểu diễn bởi 2 danh sách
    thực hiện phép cộng 2 số a, b trên 2 danh sách theo quy tắc cộng thông thường. kết quả trả về là 1 danh sách biểu diễn tổng a+b
    ví dụ
    a = [1,2,4,5]
    b =   [7,8,9]

    c = [2,0,3,4]
    """
    numa = ""
    for i in a:
        numa += str(i)
    numb = ""
    for i in b:
        numb += str(i)
    numc = str(int(numa) + int(numb))
    c = []
    for i in numc:
        c.append(int(i))
    return c


# print(addNum([1, 2, 4, 5], [7, 8, 9]))
