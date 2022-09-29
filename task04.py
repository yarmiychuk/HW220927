# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

fileName = 'file.txt'

def createList(num):

    list = []

    for i in range(num):
        list.append(randint(-num, num))

    return list


def writePositionsToFile(num):

    with open(fileName, "w") as f:
        for i in range(2):
            f.write(str(randint(0, num - 1)) + '\n')


def getIndexesFromFile():

    list = []

    with open(fileName, "r") as f:
        for i in range(2):
            list.append(int(f.readline()))

    return list


numbers = createList(int(input('Введите размер списка (3 - 10): ')))
print(f'Список элементов: {numbers}')

writePositionsToFile(len(numbers))

indexes = getIndexesFromFile()
print(f'Выбранные случайные позиции: {indexes[0]} и {indexes[1]}')

print(f'Произведение элементов с этими позициями равно: {numbers[indexes[0]] * numbers[indexes[1]]}')