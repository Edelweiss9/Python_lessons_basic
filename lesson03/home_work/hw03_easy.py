# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    frac = number % 1 * (10 ** ndigits)
    rem = frac % 1

    if rem * 2 >= 1:
        rem = 1
    else:
        rem = 0

    frac = frac // 1 + rem

    if int(frac) == 100000:
        number = str(int(number // 1 + 1)) + ('.' + str((frac / (10 ** ndigits)))[2:])
    else:
        number = str(int(number // 1)) + ('.' + str((frac / (10 ** ndigits)))[2:])

    return float(number)


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    numbers = [int(n) for n in str(ticket_number)]
    return True if sum(numbers[:3]) == sum(numbers[3:]) else False


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
