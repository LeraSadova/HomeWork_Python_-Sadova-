# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
print("Зададим список из n чисел последовательности $(1+\frac 1 n)^n$")

n = int(input('Введи число N: \n')) 

def sequence(n): #последовательность

    return[round((1 + 1 / x)**x, 4) for x in range (1, n + 1)]   
        
print(sequence(n))
print(round(sum(sequence(n))))