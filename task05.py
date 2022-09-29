# Реализуйте алгоритм перемешивания списка.

from random import randint

def shiffle(list):

    lenght = len(list)

    for i in range(lenght):
        rnd = randint(0, lenght - 1)
        temp = list[i]
        list[i] = list[rnd]
        list[rnd] = temp
    
    return list

def createList(num):

    list = []

    for i in range(num):
        list.append(randint(0, 100))

    return list

print ('Перемешивание списка чисел')
numbers = createList(int(input('Введите размер списка: ')))
print(f'Созданный список: {numbers}')
print(f'Перемешанный список: {shiffle(numbers)}')
