#Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

number = int(input('введите число n: '))
list = []
for i in range(1, number + 1):
    list.append((1 + 1 / i) ** i)
print(sum(list))
