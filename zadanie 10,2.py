my_dict = {}
for n in range(10, -6, -1):
    my_dict[n] = n ** n

# Выводим результат для проверки
for key, value in my_dict.items():
    print(f"{key}: {value}")