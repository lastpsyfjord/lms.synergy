number = int(input())

# Разбираем число на цифры (по разрядам)
units = number % 10           # единицы
tens = (number // 10) % 10    # десятки
hundreds = (number // 100) % 10  # сотни
thousands = (number // 1000) % 10  # тысячи
tens_of_thousands = number // 10000  # десятки тысяч

# Выполняем вычисления по шагам
step1 = tens ** units        # десятки в степени единиц
step2 = step1 * hundreds     # умножаем на сотни
step3 = tens_of_thousands - thousands  # разность старших разрядов

# Проверяем деление на ноль и выводим результат
if step3 == 0:
    print(0.0)
else:
    result = step2 / step3
    print(result)