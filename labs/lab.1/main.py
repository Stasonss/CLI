import math
import numpy as np

try:

    number = int(input("Введіть номер завдання з лабораторної роботи: "))
    if number < 1 or number > 3:
          print("Невірний номер завдання")


    if number == 1:

        A_deg = float(input("Введіть значення кута A в градусах: "))

        A_rad = math.radians(A_deg)

        z = math.cos(A_rad) + math.sin(A_rad) + math.cos(3 * A_rad) + math.sin(3 * A_rad)

        print(f"Значення виразу z для кута A = {A_deg} градусів: {z}")


    elif number == 2:
        
        def fibonacci(n):
    
            if n == 0 or n == 1 or n == 2:
                return 1
            
            a, b = 1, 1  
            for i in range(3, n + 1):
                a, b = b, a + b
            return b


        n = int(input("Введіть число n: "))
        print(f"{n}-й елемент послідовності Фібоначчі: {fibonacci(n)}")


    elif number == 3: 

        matrix = np.array([[1, 2, 3, 4],
                        [5, 6, 7, 8],
                        [9, 10, 11, 12],
                        [13, 14, 15, 16],
                        [17, 18, 19, 20]])

        print("Початкова матриця:")
        print(matrix)

        matrix[[0, 2]] = matrix[[2, 0]]


        print("\nМатриця після зміни місцями першого і третього рядків:")
        print(matrix)



except ValueError:
        print("Вводьте цифри!")