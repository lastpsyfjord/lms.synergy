def print_list(lst):
    if not lst:  # Если список пуст
        print("Конец списка")
        return
    print(lst[0])  # Выводим первый элемент
    print_list(lst[1:])  # Рекурсия для подсписка без первого элемента

# Пример использования
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print_list(my_list)