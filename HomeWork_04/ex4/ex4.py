# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
# открываем для записи файл
def write_file(st):
    with open('HomeWork4_ex4.txt', 'w') as data:
        data.write(st)

def rnd():
    # берем 101, т.к. правая граница не входит
    return random.randint(0,101) 

def create_mn(k):
    lst = [rnd() for i in range(k+1)]
    return lst
  
def create_str(sp):
    spisok= sp[::-1]
    wr = ''
    if len(spisok) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(spisok)):
            if i != len(spisok) - 1 and spisok[i] != 0 and i != len(spisok) - 2:
                wr += f'{spisok[i]}x^{len(spisok)-i-1}'
                if spisok[i+1] != 0:
                    wr += ' + '
            elif i == len(spisok) - 2 and spisok[i] != 0:
                wr += f'{spisok[i]}x'
                if spisok[i+1] != 0:
                    wr += ' + '
            elif i == len(spisok) - 1 and spisok[i] != 0:
                wr += f'{spisok[i]} = 0'
            elif i == len(spisok) - 1 and spisok[i] == 0:
                wr += ' = 0'
    return wr

k = int(input("Введите натуральную степень k = "))
koef = create_mn(k)
write_file(create_str(koef))