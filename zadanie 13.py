import random  # Подключаем модуль для случайных чисел

# Создаём первую матрицу 10x10
matrix1 = []  # Пустой список для матрицы
for i in range(10):  # 10 строчек
    row = []  # Новая строчка
    for j in range(10):  # 10 чисел в строчке
        # Добавляем случайное число от -100 до 100
        row.append(random.randint(-100, 100))
    matrix1.append(row)  # Добавляем строчку в матрицу

# Создаём вторую матрицу 10x10
matrix2 = []  # Пустой список для второй матрицы
for i in range(10):  # Снова 10 строчек
    row = []  # Новая строчка
    for j in range(10):  # 10 чисел
        # Добавляем случайное число
        row.append(random.randint(-100, 100))
    matrix2.append(row)  # Добавляем строчку

# Создаём матрицу для суммы
matrix3 = []  # Пустой список для суммы
for i in range(10):  # Для каждой строчки
    new_row = []  # Новая строчка для суммы
    for j in range(10):  # Для каждого числа в строчке
        # Складываем числа из первой и второй матрицы
        sum_element = matrix1[i][j] + matrix2[i][j]
        new_row.append(sum_element)  # Добавляем сумму в строчку
    matrix3.append(new_row)  # Добавляем строчку в результат

# Выводим все матрицы (можно закомментировать, если слишком длинно)
print("Первая матрица:")
for row in matrix1:
    print(row)

print("\nВторая матрица:")
for row in matrix2:
    print(row)

print("\nСумма матриц:")
for row in matrix3:
    print(row)