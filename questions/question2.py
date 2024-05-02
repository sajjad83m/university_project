def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f


def binary_compar(num, func):
    index_i = 0
    index_f = num

    while index_i + 1 < index_f:
        index_mid = (index_i + index_f) // 2
        if num == func(index_mid):
            return index_mid
        elif num > func(index_mid):
            index_i = index_mid
        elif num < func(index_mid):
            index_f = index_mid
    else:
        return index_i


def q2(number):
    f_list = []
    while number != 0:
        f = binary_compar(number, factorial)
        number = number - factorial(binary_compar(number, factorial))
        f_list.append(f)

    ret_str = ''
    for f in f_list:
        ret_str += str(f) + '! '
    return ret_str
