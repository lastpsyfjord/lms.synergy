n = int(input().strip())  
arr = []                   

# Считываем n чисел и добавляем их в список
for _ in range(n):
    num = int(input().strip())
    arr.append(num)

# Переворачиваем список
reversed_arr = arr[::-1]

# Выводим каждый элемент перевернутого списка на новой строке
for num in reversed_arr:
    print(num)