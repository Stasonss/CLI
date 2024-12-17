class Book:
    def __init__(self, title, author, year, genre=None):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def __str__(self):
        return f"{self.title}, автор: {self.author} ({self.year}), жанр: {self.genre or 'немає'}"

class Biblioteka:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, index):
        if 0 <= index < len(self.books):
            self.books.pop(index)

    def search_books(self, title=None, author=None, year=None, genre=None):
        results = []
        for book in self.books:
            if (title and title.lower() not in book.title.lower()) or \
               (author and author.lower() not in book.author.lower()) or \
               (year and year != book.year) or \
               (genre and genre.lower() not in (book.genre or "").lower()):
                continue
            results.append(book)
        return results

    def display_books(self):
        if not self.books:
            print("Бібліотека порожня.")
        for i, book in enumerate(self.books):
            print(f"{i + 1}. {book}")

biblioteka = Biblioteka()

while True:
    print("\nМеню:")
    print("1. Додати книгу")
    print("2. Видалити книгу")
    print("3. Пошук книги")
    print("4. Відобразити всі книги")
    print("5. Вийти\n")

    choice = input("Виберіть опцію (1-5): ")

    if choice == '1':
        title = input("Введіть назву книги: ")
        author = input("Введіть автора книги: ")
        year = int(input("Введіть рік видання книги: "))
        genre = input("Введіть жанр книги (або залиште порожнім): ")
        book = Book(title, author, year, genre if genre else None)
        biblioteka.add_book(book)

    elif choice == '2':
        biblioteka.display_books()
        index = int(input("Введіть номер книги для видалення: ")) - 1
        biblioteka.remove_book(index)

    elif choice == '3':
        keyword = input("Введіть параметр для пошуку (title, author, year, genre): ").strip()

        if keyword not in ['title', 'author', 'year', 'genre']:
            print("Помилка: недійсний параметр для пошуку. Спробуйте ще раз.")
        else:
            value = input(f"Введіть значення для пошуку по {keyword}: ").strip()
        
            if keyword == 'year':
                value = int(value)

            results = biblioteka.search_books(**{keyword: value})
            if results:
                print("Знайдені книги:")
                for book in results:
                    print(book)
            else:
                print("Книгу не знайдено.")

    elif choice == '4':
        biblioteka.display_books()

    elif choice == '5':
        print("До побачення!")
        break

    else:
        print("Невірний вибір. Спробуйте ще раз.")