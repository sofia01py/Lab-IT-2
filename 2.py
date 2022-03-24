import re
from functions import *


input_txt = input('ur word: ')
input_txt = text_to_bits(input_txt)
print(input_txt)
i = []
for k,l in enumerate(input_txt):
    if int(l) == 1:
        i.append(k)
print(i)

a = 0
expression = input('number of summators: ')
if testing_expression_summators(expression) == True:
    summators = int(expression)
    g = []
    while summators != 0:
        m = []
        expression = input("Введите позиции от 1 до 3 в сумматоре подряд без пробелов(пример:'23'): ")
        if testing_expression_positions(expression) == True:
            positions = expression
            m = list(positions)
            g.append(m)
        else:
            print("Error! Incorrect expression!")
        summators -= 1
    m = 0
    for k, m in enumerate(g):
        for l, n in enumerate(g[k]):
            g[k][l] = int(g[k][l]) - 1
    # print(g)
    c = []
    a = []
    for k, m in enumerate(g):
        for l, n in enumerate(g[k]):
            for p, q in enumerate(i):
                d = int(n) + int(q)
                a.append(d)
        a = sorted(a)
        c.append(a)
    print(c)
    w = 0
    z = []
    count = 0
    code_word = []
    for k, m in enumerate(c):
        for l, n in enumerate(c[k]):
            if n == n + 1:
                if count == 0:
                    count += 1
                else:
                    count = 0
            else:
                z.append(n)
        code_word.append(z)
    print(code_word)







    print(c)

else:
    print('Error! Incorrect number of summators!')

