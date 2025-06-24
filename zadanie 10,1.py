def get_age_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        return 'год'
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
        return 'года'
    else:
        return 'лет'

pets = {}
num_pets = int(input("Введите количество питомцев: "))

for _ in range(num_pets):
    name = input("Введите имя питомца: ")
    animal_type = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner = input("Введите имя владельца: ")
    
    pets[name] = {
        'Вид питомца': animal_type,
        'Возраст питомца': age,
        'Имя владельца': owner
    }

print("\nИнформация о питомцах:")
for pet_name in pets.keys():
    pet_data = pets[pet_name]
    animal_type = pet_data['Вид питомца']
    age = pet_data['Возраст питомца']
    owner = pet_data['Имя владельца']
    age_suffix = get_age_suffix(age)
    
    print(f'Это {animal_type} по кличке "{pet_name}". Возраст питомца: {age} {age_suffix}. Имя владельца: {owner}')