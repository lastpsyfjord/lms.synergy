n = int(input())
arr = list(map(int, input().split()))
if n > 1:
    arr = [arr[-1]] + arr[:-1]
print(" ".join(map(str, arr)))