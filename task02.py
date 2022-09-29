# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N

def getFacorial(num):
    factorial = []
    current = 1
 
    for i in range(1, num + 1):
        current *= i
        factorial.append(current)
    
    return factorial

print('Вычисление набора произведений (факторилов) от 1 до N')
number = int(input('Введите целое число N: '))
print(f'Результат: {getFacorial(number)}')