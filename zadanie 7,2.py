s = input()
result = ""
for char in s:
    if char != ' ':
        result += char
    else:
        if result == "" or result[-1] != ' ':
            result += char
print(result)