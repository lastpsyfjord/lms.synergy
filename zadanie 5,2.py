word = input().strip().lower()  # Ввод слова и приведение к нижнему регистру

# Инициализация
vowels_count = 0
consonants_count = 0
specific_vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

# Подсчет букв
for letter in word:
    if letter in specific_vowels:
        vowels_count += 1
        specific_vowels[letter] += 1
    else:
        consonants_count += 1

# Вывод результата
print(f"Гласных: {vowels_count}")
print(f"Согласных: {consonants_count}")

# Вывод количества каждой гласной
for vowel in 'aeiou':
    print(f"{vowel}: {specific_vowels[vowel]}")

# Проверка наличия всех гласных
if all(specific_vowels.values()):
    pass  # Если все гласные есть, ничего не делаем
else:
    print(False)