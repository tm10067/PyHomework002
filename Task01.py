# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# 0,56 -> 11

# ЧЕРЕЗ СТРОКУ

# number = input('введите число: ')
# print (number)
# digit_sum = 0
# for i in range(len(number)):
#     if number[i] == '-' or number[i] == '.':
#         continue
#     else:    
#         digit_sum += int(number[i])
# print(digit_sum)

# ЧЕРЕЗ ЧИСЛА

number = float(input('введите число: '))

def float_to_int(float_number):
    while round(float_number, 8) != int(float_number):
        float_number *= 10
    int_number = int(float_number)
    return int_number

def sum_digit (number):
    int_number = abs(int(number))
    digit_sum = 0
    while int_number >= 1:
        digit_sum += int_number % 10
        int_number //= 10
    return digit_sum

print(sum_digit(float_to_int(number)))
