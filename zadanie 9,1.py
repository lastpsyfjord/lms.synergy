n = int(input().strip())
numbers = set(map(int, input().split()[:n]))
print(len(numbers))