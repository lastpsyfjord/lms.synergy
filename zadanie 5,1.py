n = int(input().strip())

if n == 0:
    print("нулевое число")
elif n % 2 == 0:
    if n > 0:
        print("положительное четное число")
    else:
        print("отрицательное четное число")
else:
    print("число не является четным")