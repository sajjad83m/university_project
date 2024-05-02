str_out = []
def q7(before_str, Main_str):
    if len(before_str) + 1 == len(Main_str):
        for char0 in Main_str:
            if str.count(before_str, char0) == 0:
                str_out.append(before_str + char0)
        return str_out
    else:
        for char0 in Main_str:
            if str.count(before_str, char0) == 0:
                str_out.append(before_str + char0)
                q7(before_str + char0, Main_str)
        return str_out


#array = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#
#
#def combination(before_str, array, lenght):
#    if lenght == 1:
#        for i in array:
#            print(before_str + i)
#    for i in range(0, len(array)):
#        combination(before_str + array[i], array[i + 1::], lenght - 1)
#
#
#combination('', array, 2)