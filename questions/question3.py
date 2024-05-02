def q3(lst):
    a = lst[0]
    for i in range(1, len(lst)):
        b = lst[i]
        comb = a * b
        while b > 0:
            rem = a % b
            a = b
            b = rem
        gcd = a
        lcm = comb // gcd
        a = lcm
    return lcm
