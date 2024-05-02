from questions.question1 import q1
from questions.question2 import q2
from questions.question3 import q3
from questions.question4 import q4
from questions.question5 import q5
from questions.question6 import q6
from questions.question7 import q7
from questions.question8 import q8
from questions.question9 import q9
from questions.question10 import q10

def p1():
    number = int(input('please enter your number: '))
    lst = q1(number)
    print(lst)

def p2():
    number = int(input('please enter your number: '))
    str_out = q2(number)
    print(str_out)

def p3():
    lst_in = input('please enter your numbers with espace between them: ').split()
    for i in range(0,len(lst_in)):
        lst_in[i] = int(lst_in[i])
    num_out = q3(lst_in)
    print(num_out)

def p4():
    teams = input('please enter the name of teams with espace between them: ').split()
    dic = {}
    for team1 in teams:
        dic_r = {}
        for team2 in teams:
            if team1 != team2:
                result = int(input(f'\t-the result of {team1} with {team2}-\n if {team1} win enter 1 if loose -1 if equal 0: '))
                dic_r.update({team2: result})
        dic.update({team1: dic_r})
        
    for i in q4(dic):
        print(i)
    
def p5():
    f_num = int(input('please choose a function with enter an number between 1,2,3:\n1-sin(x)\n2-radical(x)\n3-sigma\n'))
    if f_num == 1:
        func = 'sin'
    if f_num == 2:
        func = 'radical'
    if f_num == 3:
        func = 'sigma'
        
    a = int(input('please enter the lower limit of the integration (a): '))
    b = int(input('please enter the upper limit of the integration (b): '))
    n = int(input('please enter the n: '))
    print(q5(a, b, n, func))
    
def p6():
    city_x = int(input("please enter the Lenght of city 'x': "))
    city_y = int(input("please enter the width of city 'y' : "))
    store1_x = int(input("please enter the x of first store: "))
    store1_y = int(input("please enter the y of first store: "))
    store2_x = int(input("please enter the x of second store: "))
    store2_y = int(input("please enter the y of first store: "))
    store3_x = int(input("please enter the x of third store: "))
    store3_y = int(input("please enter the y of third store: "))
    points = q6(city_x, city_y, store2_x, store1_y, store2_x, store2_y, store3_x, store3_y)
    str_out = ''
    str_out += f'the vertices of first store is {points[0]}\nthe vertices of second store is {points[1]}\nthe vertices of third store is {points[2]}'
    print(str_out)

def p7():
    str_in = input('please enter your string: ')
    out = q7('', str_in)
    print(out)

def p8():
    str_in = input('please enter your sentence: ')
    num_out = q8(str_in)
    print(num_out)

def p9():
    s_num = int(input('please enter the number of scientists: '))
    list_in = []
    for s in range(0, s_num):
        lst = []
        name = input(f'please enter the name of {s+1}th scientist: ')
        born = int(input(f"please enter the year of {name}'s born: "))
        death = int(input(f"please enter the year of {name}'s death: "))
        lst = [born, death, name]
        list_in.append(lst)
    print(q9(list_in))

def p10():
    le = int(input('please enter the number of Rows or columns (the rows and columns should be same becuase the matrix should be a square matrix): '))
    matrix = []
    print('--coefficients matrix--')
    for i in range(0, le):
        row = []
        for j in range(0, le):
            e = int(input(f"please enter the number of element at the {i+1}th row and {j+1}th column of the matrix: "))
            row.append(e)
        matrix.append(row)
        
    print('---------------------')
    print('--right side vector--')
    vector = []
    for i in range(0, le):
        e = int(input(f'please enter the {i+1}th element of right side vector: ')) 
        vector.append(e)
    
    print(q10(matrix, vector))

p_num = int(input('which program do you want to run? enter a number between 1-10: '))

match p_num:
    case 1:
        p1()
    case 2:
        p2()
    case 3:
        p3()
    case 4:
        p4()
    case 5:
        p5()
    case 6:
        p6()
    case 7:
        p7()
    case 8:
        p8()
    case 9:
        p9()
    case 10:
        p10()