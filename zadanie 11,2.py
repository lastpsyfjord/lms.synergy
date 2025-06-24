pets = {
    1: {"Мухтар": {"Вид питомца": "Собака", "Возраст питомца": 9, "Имя владельца": "Павел"}},
    2: {"Каа": {"Вид питомца": "желторотый питон", "Возраст питомца": 19, "Имя владельца": "Саша"}}
}

def get_suffix(age):
    """Правильное окончание для слова 'год'"""
    if 11 <= age <= 19:
        return "лет"
    last_digit = age % 10
    if last_digit == 1:
        return "год"
    elif 2 <= last_digit <= 4:
        return "года"
    else:
        return "лет"

def get_pet(ID):
    """Проверяет есть ли питомец с таким ID"""
    if ID in pets:
        return pets[ID]
    else:
        return False

def pets_list():
    """Показывает всех питомцев"""
    print("\nВсе питомцы в базе:")
    for id, pet in pets.items():
        name = list(pet.keys())[0]
        print(f"ID: {id}, Кличка: {name}")
    print()

def create():
    """Добавляет нового питомца"""
    if pets:
        new_id = max(pets.keys()) + 1
    else:
        new_id = 1
    
    name = input("Введите кличку питомца: ")
    animal_type = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner = input("Введите имя владельца: ")
    
    pets[new_id] = {
        name: {
            "Вид питомца": animal_type,
            "Возраст питомца": age,
            "Имя владельца": owner
        }
    }
    print(f"\nПитомец {name} добавлен с ID {new_id}!\n")

def read(ID):
    """Показывает информацию о питомце"""
    pet = get_pet(ID)
    if not pet:
        print(f"\nПитомца с ID {ID} нет в базе\n")
        return
    
    name = list(pet.keys())[0]
    animal_type = pet[name]["Вид питомца"]
    age = pet[name]["Возраст питомца"]
    owner = pet[name]["Имя владельца"]
    
    suffix = get_suffix(age)
    print(f'\nЭто {animal_type} по кличке "{name}". Возраст: {age} {suffix}. Владелец: {owner}\n')

def update(ID):
    """Изменяет информацию о питомце"""
    pet = get_pet(ID)
    if not pet:
        print(f"\nПитомца с ID {ID} нет в базе\n")
        return
    
    name = list(pet.keys())[0]
    print(f"\nИзменяем питомца {name} (ID: {ID}):")
    
    new_name = input(f"Новая кличка ({name}): ") or name
    new_type = input(f"Новый вид ({pet[name]['Вид питомца']}): ") or pet[name]["Вид питомца"]
    new_age = input(f"Новый возраст ({pet[name]['Возраст питомца']}): ") or pet[name]["Возраст питомца"]
    new_owner = input(f"Новый владелец ({pet[name]['Имя владельца']}): ") or pet[name]["Имя владельца"]
    
    # Обновляем данные
    del pets[ID][name]
    pets[ID][new_name] = {
        "Вид питомца": new_type,
        "Возраст питомца": int(new_age),
        "Имя владельца": new_owner
    }
    print("\nДанные обновлены!\n")

def delete(ID):
    """Удаляет питомца из базы"""
    if ID in pets:
        name = list(pets[ID].keys())[0]
        del pets[ID]
        print(f"\nПитомец {name} (ID: {ID}) удалён\n")
    else:
        print(f"\nПитомца с ID {ID} нет в базе\n")

# Основная программа
print("База данных ветеринарной клиники")
while True:
    command = input("Введите команду (create, read, update, delete, list, stop): ").lower()
    
    if command == "stop":
        print("Работа завершена")
        break
        
    elif command == "create":
        create()
        
    elif command == "read":
        try:
            ID = int(input("Введите ID питомца: "))
            read(ID)
        except:
            print("Ошибка! Введите число")
            
    elif command == "update":
        try:
            ID = int(input("Введите ID питомца: "))
            update(ID)
        except:
            print("Ошибка! Введите число")
            
    elif command == "delete":
        try:
            ID = int(input("Введите ID питомца: "))
            delete(ID)
        except:
            print("Ошибка! Введите число")
            
    elif command == "list":
        pets_list()
        
    else:
        print("Неизвестная команда. Попробуйте снова")