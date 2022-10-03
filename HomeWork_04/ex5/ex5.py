# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

#не решила как просите. Напишу алгоритм просто для сложения чисел из двух файлов

from turtle import st


numbers1 = ['100']
data = open ('HW4_ex5_01.txt', 'a')
data.writelines(numbers1)
data.close()

numbers2 = ['250']
data = open ('HW4_ex5_02.txt', 'a')
data.writelines(numbers2)
data.close()

# пыталась я в инт перевестич исла из файла
# num1=int(numbers1)
# num2=int(numbers2)
# num3=num1+num2

numbers3 = numbers1+numbers2
data = open ('HW4_ex5_03.txt', 'a')
data.writelines(numbers3)
data.close()
