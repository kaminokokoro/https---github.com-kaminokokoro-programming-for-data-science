# Hoàn thiện các phương thức trong file Fraction.py theo các mô tả sau:

# Hàm is_minimalist_fraction(numerator, denominator) kiểm tra phân số gồm tử số là numerator, và mẫu số là denominator có phải phân số tối giản hay không nếu đúng trả lại giá trị là True, ngược lại trả lại giá trị là False?
import math


def is_minimalist_fraction(numerator, denominator):
    if math.gdc(numerator, denominator) == 1 or numerator == 0:
        return True
    return False


# Hàm get_minimalist_fraction(numerator, denominator) thực hiện tính và trả lại phân số tối giản của phân số đầu vào (phân số được trả lại là 2 giá trị tương ứng là tử số và mẫu số)


def get_minimalist_fraction(numerator, denominator):
    if is_minimalist_fraction(numerator, denominator):
        return numerator, denominator
    return numerator // math.gdc(numerator, denominator), denominator // math.gdc(
        numerator, denominator
    )
