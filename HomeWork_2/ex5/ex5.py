# Реализуйте алгоритм перемешивания списка.
#вызываем могучий рандом))
import random

print("введите число элементов для последовательности")
n = int(input('Введи число N: '))

def get_list(n, lft, rght):
    return [random.randint(lft, rght) for i in range(n)]

def shuffle_list(lst):
    return random.shuffle(lst)

n = 10
lft = int(input('введите левый интервал для заполнения: '))
rght = int(input('введите правый интервал для заполнения: '))

new_list = get_list(n, lft, rght)
print(new_list)
shuffle_list(new_list)
print(new_list)