import os
import sys

if len(sys.argv) < 2:
    print("Введіть команду 'list' або 'run' з номером лабораторної!")
    sys.exit(1)

else:
    command = sys.argv[1]

    if command == "list":

        dir = os.listdir("labs/")
        list_labs = False

        for i, dir1 in enumerate(dir, 1):
            if dir1.startswith("lab."):
                if not list_labs:
                    print("Доступні лабораторні роботи:")
                    list_labs = True
                i = dir1[4:]
                print(f"{i}. {dir1} - Лабораторна робота №{i}")
        if not list_labs:
            print("Нема доступних робіт")


    elif command == "run":
        if len(sys.argv) < 3:
            print("Введіть номер лабораторної після команди run!")
            sys.exit(1)

        lab_number = sys.argv[2]
        lab_number = int(lab_number)
        lab_name = f"lab.{lab_number}"

        try:
            if not os.path.exists(f"labs/{lab_name}") or lab_number == 0:
                print(f"Лабораторна робота №{lab_number} недоступна.")

            else:
                print(f"Запуск лабораторної роботи №{lab_number}...")
                os.system(f"python labs/{lab_name}/main.py")
                print("Результат: Лабораторна виконана успішно!")
        except ValueError:
            print("Вводьте цифри!")

    else:
        print(f"Невірна команда!")




