# Задайте список из n чисел последовательности (1+1/n)^n
# и выведите на экран их сумму.

def getList(n):
    list = []

    for i in range(1, n + 1):
        list.append((1 + 1 / i) ** i)

    return list

def getSum(list):
    sum = 0

    for i in range (len(list)):
        sum += list[i]

    return sum

print('Вычисление суммы чисел последовательности (1+1/n)^n')
n = int(input('Введите число N: '))

list = getList(n)
print (f'Список чисел: {list}')
print (f'Сумма этих чисел: {getSum(list)}')