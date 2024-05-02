def power(x, n):
    x2 = x
    if n == 0:
        return 1
    for i in range(1, n):
        x2 = x2 * x
    return x2

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


def q5(a, b, n, func_name):

    def sin(x):
        def taylor_series_sin(x):
            sum = 0
            for n in range(1, 50):
                sum += power(-1, n) * power(x, 2 * n + 1) / factorial(2 * n + 1)
            return sum

        pi = 3.14
        out = x % pi                    # sin(a + k*pi) = sin(a), (k = 2n)  #sin(a + k*pi) = -sin(a), (k = 2n+1)
        if (x // pi) % 2 != 0:          # so when we devide 'x' to pi, if outside be even sin(x) = sin(x%2)
            out = -out                  # and if outside be odd sin(x) = -sin(x%2) and we know -sin(x) = sin(-x)
                                        # also we can do that just with divide to 2*pi
        return taylor_series_sin(out)

    def radical(x):

        def x_power2(x):
            return power(x, 2)

        n = binary_compar(x, x_power2)
        a = x_power2(n)
        rem = x - a
        f = n  #'f' is equal with radical a
        x = rem / a

        sum = 0
        for n in range(0, 30):
            sum += power(-1, n - 1) * factorial(2 * n) * power(x, n) / (
                (2 * n - 1) * power(factorial(n), 2) * power(4, n))
        return sum * f

    lst_sentences = []
    def sigma(x):
        sum = 0
        for i in range(0, len(lst_sentences)):
            sum += lst_sentences[i][0] * power(x, lst_sentences[i][1])
        return sum

    if func_name == 'sin':
        func = sin
    elif func_name == 'radical':
        func = radical
    elif func_name == 'sigma':
        func = sigma
        num = int(input("how many sentences dose the polynomial have? "))
        for i in range(0, num):
            coeff = int(input(f"please enter the coefficient of {i+1}th polynomial's sentence: "))
            pow = int(input(f"please enter the degree of {i+1}th polynomial's sentence: "))
            lst_sentences.append([coeff, pow])
    
    h = (b - a) / n
    sum = 0
    for i in range(1, n - 1):
        sum += func(a + i * h)
    I = (h / 2)*(func(a) + 2*sum + func(b))
    return I
