# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# Мой стандартный код для ввода массивы с клавиатуры
n = int(input("Задайте количество элементов в списке: "))
print("теперь введем элементы списка (целые числа, иначе будет ошибка)")
spisok = [] #объявление списка
#заполняем наш список:
spisok = [int(input(f"введите {i+1} целое число: ")) for i in range(n)] 
print ("Введенный с клавиатуры список имеет вид: ")
print (spisok, end=" ")
print()

# объявляем новый список, куда положим неповторяющие элементы:
new_spisok = []

[new_spisok.append(j) for j in spisok if j not in new_spisok]
print(f"Список неповторяющихся элементов из ранее заданного массива: {new_spisok}")
