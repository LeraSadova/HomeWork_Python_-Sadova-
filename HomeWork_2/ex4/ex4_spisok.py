# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

print("Зададим список из N элементов из промежутка [-N, N]")
n = int(input('Введи число N: '))
list_for_n = []

for i in range(-n,n+1):
    list_for_n.append(i)
print(list_for_n) #выводим полученный список

result = 1 #изначально произведение равно 1
with open('file.txt','w') as data:
    #выбираем номера элементов. Задаем их и храним в файле
    data.write('0 \n')
    data.write('2 \n')
    data.write('4 \n')
    data.write('6 \n')
    data.write('8 \n')
    data.write('10 \n')
    data.write('12 \n')
    
patch = 'file.txt'
data = open(patch, 'r')

for line in data: #для строки в файле
    position = int(line) #выбираем порядок элемента из файла
    result *= list_for_n[position] #перемножаем выбранные позиции из массива
print("Произвдение элементов под индексами 0, 2, 4, 6, 8, 10, 12:")
print(result)