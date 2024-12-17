import numpy as np
import matplotlib.pyplot as plt
import re
from collections import Counter


try:

    zavd = int(input("Введіть номер завдання (1-3): "))


    if zavd == 1:

        x = np.linspace(-2, 5, 400)
        y = x * np.sin(5 * x)

        plt.plot(x, y)
        plt.title(r'$Y(x) = x \cdot \sin(5x)$')
        plt.xlabel('x')
        plt.ylabel('Y(x)')
        plt.grid(True)

        plt.savefig('labs/lab.7/graph.png')

        plt.show()


    elif zavd == 2:

        text = input("Введіть текст: ")

        text = text.lower()
        text = text.replace(" ", "")

        letter_counts = Counter(text)

        letters = list(letter_counts.keys())
        counts = list(letter_counts.values())

        plt.bar(letters, counts, color='red')

        plt.title("Частота появи літер у тексті")
        plt.xlabel("Літери")
        plt.ylabel("Частота")

        plt.savefig('labs/lab.7/histogram.png')

        plt.show()

    elif zavd == 3:

        text = input("Введіть текст: ")

        punctuations = ['.', '!', '?', '...']
        sentences = []
        sentence = ""
        i = 0

        while i < len(text):
            if text[i:i+3] == '...':
                sentences.append(sentence.strip() + '...')
                sentence = ""
                i += 3
            elif text[i] in punctuations:
                sentences.append(sentence.strip() + text[i])
                sentence = ""
                i += 1
            else:
                sentence += text[i]
                i += 1

        regular_sentences = 0
        question_sentences = 0
        exclamation_sentences = 0
        ellipsis_sentences = 0

        for sentence in sentences:
            if sentence.endswith('?'):
                question_sentences += 1
            elif sentence.endswith('!'):
                exclamation_sentences += 1
            elif sentence.endswith('...'):
                ellipsis_sentences += 1
            else:
                regular_sentences += 1

        sentence_types = ['Звичайні', 'Питальні', 'Окличні', 'Трикрапка']
        counts = [regular_sentences, question_sentences, exclamation_sentences, ellipsis_sentences]

        plt.bar(sentence_types, counts)

        plt.title("Частота появи типів речень у тексті")
        plt.xlabel("Типи речень")
        plt.ylabel("Кількість речень")

        plt.savefig('labs/lab.7/histogram2.png')

        plt.show()


    else:
        print("Невірний номер завдання")

except ValueError:
    print("Введьте цілі числа")

