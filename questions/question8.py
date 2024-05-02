
def q8(string):
    #string = '* + 2 3 - 9 4'
    r_str = string[::-1]
    operators = ['*', '+', '-', '/']
    
    numbers = []
    r_str_list = r_str.split()
    for str_ in r_str_list:
        if str.isdigit(str_):
            numbers.append(int(str_))
        elif operators.count(str_) != 0:
            number1 = numbers[-1]
            number2 = numbers[-2]
            if str_ == '/':
                result = number1 / number2

            elif str_ == '//':
                result = number1 // number2

            elif str_ == '*':
                result = number1 * number2

            elif str_ == '**':
                result = number1**number2

            elif str_ == '+':
                result = number1 + number2

            elif str_ == '-':
                result = number1 - number2

            numbers.append(result)
            numbers.remove(number1)
            numbers.remove(number2)
    return result