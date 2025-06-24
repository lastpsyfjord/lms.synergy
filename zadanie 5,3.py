x = int(input().strip())  # Минимальная сумма инвестиций
a = int(input().strip())  # Деньги Майкла
b = int(input().strip())  # Деньги Ивана

if a >= x and b >= x:
    print(2)
elif a >= x:
    print("Mike")
elif b >= x:
    print("Ivan")
elif a + b >= x:
    print(1)
else:
    print(0)