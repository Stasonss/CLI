def read_file(file_name):
    try:
        with open(f"labs/lab.3/{file_name}", 'r') as file_local:
            datas = file_local.readlines()
            return datas
    except FileNotFoundError:
        create = input(f"Файл {file_name} не знайдено. Хочете його створити? (так/ні): ")
        if create.lower() == 'так':
            with open(f"labs/lab.3/{file_name}", 'w') as file_local:
                file_local.write("")  
            print(f"Файл {file_name} успішно створено.")
            return []
        else:
            print("Файл не був створений.")
            return []

def write_file(file_name, data):
        with open(f"labs/lab.3/{file_name}", 'w') as file_local:
            file_local.writelines(data)