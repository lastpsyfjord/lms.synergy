A = int(input())
B = int(input())

if A % 2 != 0:
    A += 1

if A > B:
    pass
else:
    print(A, end='')
    A += 2
    while A <= B:
        print('', A, end='')
        A += 2
    print()