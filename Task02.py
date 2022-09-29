# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input('введите число N: '))
list = []

def factorial(number):
    fact = number
    if number > 1:
        fact *= factorial(number - 1) 
    return fact

for i in range(1, number + 1):
    list.append(factorial(i))
print(list)
