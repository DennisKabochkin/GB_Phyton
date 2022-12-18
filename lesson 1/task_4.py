# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input("Введите целое положительное число: "))
max_number = 0
while number != 0:
    val = number % 10
    if max_number < val:
        max_number = val
    number = number // 10
print(f"Самая большая цифра в числе: {max_number}")
