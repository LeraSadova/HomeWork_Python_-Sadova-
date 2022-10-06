# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# Я удалю слова, которые содержат букву "о"

lukomorie = 'У лукоморья дуб зелёный ; Златая цепь на дубе том : И днём и ночью кот учёный \
Всё ходит по цепи кругом ; Идёт направо — песнь заводит , Налево — сказку говорит.'
print("Исходный текст: ")
print(lukomorie)

def delite(lukomorie):
    lukomorie = list(filter(lambda x: 'о' not in x, lukomorie.split()))
    return " ".join(lukomorie)

lukomorie = delite(lukomorie)
print()
print("Текст, с удаленными словами, содержащими *о*: ")
print(lukomorie)