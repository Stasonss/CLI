import requests
from bs4 import BeautifulSoup
from collections import Counter

def analyze_news_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text
        
        soup = BeautifulSoup(html_content, 'html.parser')

        tags = [tag.name for tag in soup.find_all()]
        tag_frequency = Counter(tags)

        links = soup.find_all('a', href=True)
        link_count = len(links)

        images = soup.find_all('img', src=True)
        image_count = len(images)

        text = soup.get_text()
        words = text.lower().split()
        filtered_words = [word.strip('.,!?":;()[]{}') for word in words if word.isalnum()]
        word_frequency = Counter(filtered_words)

        print("Частота HTML-тегів:")
        for tag, freq in tag_frequency.items():
            print(f"  <{tag}>: {freq}")
        
        print(f"\nКількість посилань: {link_count}")
        print(f"Кількість зображень: {image_count}")

        print("\nЧастота слів у тексті новини:")
        for word, freq in word_frequency.most_common(10):
            print(f"  {word}: {freq}")

    except requests.exceptions.RequestException as e:
        print(f"Помилка запиту: {e}")

if __name__ == "__main__":
    url = input("Введіть URL сторінки новин: ")
    analyze_news_page(url)
