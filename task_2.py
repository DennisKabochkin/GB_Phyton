# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

sec = int(input("Введите время (сек): "))
print(f"Время в формате часы:минуты:секунды - {sec / 3600:.2f} : "
      f"{sec / 60:.2f} : {sec}")
