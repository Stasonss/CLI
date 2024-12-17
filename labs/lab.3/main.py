from function import write_file, read_file

while True:

    print("Меню:")
    print("1. Додати студента")
    print("2. Відобразити студентів")
    print("3. Знайти студента")
    print("4. Сортувати студентів за середнім балом")
    print("5. Видалити студента")
    print("6. Вийти")    

    num = int(input("Виберіть опцію (1-6): "))
    if num < 1 or num > 6:
            print("Ви вибрали не вірне число або символ, повторіть\n")
            continue

    elif num == 6 :
        break

    group = input("Введіть групу")
    group = group.__add__(".txt")

    if num == 1 :
        data = read_file(group)
        surname = input("Введіть прізвище студента ")
        avg_bal = input("Введіть середній бал ")
        data.append(surname + " " + avg_bal + "\n")
        write_file(group, data)
        print("Дані успішно додані.\n")
        continue

    elif num == 2 :
        data = read_file(group)
        for i, bezN in enumerate(data):
            bezN = bezN.strip('\n')
            print(i+1, bezN)
        print("Список виведений\n")
        continue

    elif num == 3 :
        data = read_file(group)
        shyk_student = input("Введіть шуканого студента ")
        Find = False
        for i in data: 
            if i.startswith(shyk_student):
                Find = True
                surname, avg_bal = i.strip().split(" ")
                break 
        if Find == True:
            print(f"Студент {surname} знайдений у списку з середнім балом - {avg_bal}\n")
        else:
            print("Студента нема в списку\n")
        continue
    
    elif num == 4 :
        data = read_file(group)
        sorted = []
        for i in data:
            not_sort = float(i.split(" ")[1])
            sorted.append(not_sort)
        sorted.sort(reverse=True)
        for i, bezN in enumerate(sorted):
            print(bezN)
        print("Список студентів відсортований за середнім балом\n")
        continue

    elif num == 5 :
        data = read_file(group)
        delete = int(input("Введіть номер студента для видалення "))
        if delete < 1:
                print('Номер повинен бути додатнім\n')
                continue
        index = delete - 1
        stud_delete = data[index].strip('\n')
        data.pop(index)
        print(f"Студента {stud_delete} успішно видалено\n")
        write_file(group, data)
        continue

