import random
import re
from collections import Counter


try:

    number = int(input("Введіть номер завдання з лабораторної роботи: "))
    if number < 1 or number > 2:
          print("Невірний номер завдання")


    if number == 1:




        list1 = ["Червоний", "Синій", "Зелений", "Жовтий", "Чорний"]
        list2 = ["кіт", "пес", "птах", "день", "дерево"]
        list3 = ["стрибає", "бігає", "летить", "співає", "росте"]


        def rand():
            word1 = random.choice(list1)  
            word2 = random.choice(list2)  
            word3 = random.choice(list3)  
            return f"{word1} {word2} {word3}"  


        random_phrase = rand()
        print("Випадкова фраза:", random_phrase)


    elif number == 2:

        def simvol(file_path):
            try:
                with open('labs/lab.4/text.txt', 'r',) as file:
                    text = file.read()
                    z_probilom = len(text)
                    bez_proboliv = len(text.replace(" ", ""))

                print(f"Загальна кількість символів з пробілами: {z_probilom}")
                print(f"Загальна кількість символів без пробілів: {bez_proboliv}")
            except FileNotFoundError:
                print(f"Файл {file_path} не знайдено. Перевірте правильність імені файлу.")

        simvol('labs/lab.4/text.txt')



        def analyze(file_path):
            try:
                with open('labs/lab.4/text.txt', 'r') as file:
                    text = file.read()
                
                words = re.findall(r'\b\w+\b', text.lower())

                total_words = len(words)

                unique_words = len(set(words))

                word_counts = Counter(words)

                unique_once = len([word for word, count in word_counts.items() if count == 1])
                
                print(f"Загальна кількість слів: {total_words}")
                print(f"Загальна кількість різних слів: {unique_words}")
                print(f"Кількість унікальних слів, що зустрічаються тільки один раз: {unique_once}")
            
            except FileNotFoundError:
                print(f"Файл {file_path} не знайдено. Перевірте правильність імені файлу.")

        analyze('labs/lab.4/text.txt')

        def longest_repeated(text):
            w = text.split()
            l_seq = ""
            
            for n in range(1, len(w)):
                seen = set()
                for i in range(len(w) - n + 1):
                    seq = ' '.join(w[i:i + n])
                    if seq in seen:
                        if len(seq) > len(l_seq):
                            l_seq = seq
                    seen.add(seq)

            return l_seq


        with open('labs/lab.4/text.txt', 'r', encoding='utf-8') as file:
            text = file.read()
        result = longest_repeated(text)
        print("Найдовша повторювана послідовність слів:", result)





except ValueError:
    print("Вводьте цифри!")