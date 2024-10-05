import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# URL страницы с диванами
url = "https://www.divan.ru/category/divany"

# Заголовки для запроса
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}

# Запрос к странице
response = requests.get(url, headers=headers)

# Парсим страницу
soup = BeautifulSoup(response.content, 'html.parser')

# Списки для хранения данных
product_names = []
product_prices = []

# Находим все карточки продуктов
product_cards = soup.find_all('div', {'data-testid': 'product-card'})

# Цикл по каждой карточке товара
for card in product_cards:
    # Название товара
    name_tag = card.find('a', class_='ui-GPFV8 qUioe ProductName ActiveProduct')
    if name_tag:
        product_name = name_tag.find('span', itemprop='name').text.strip()
        product_names.append(product_name)

    # Цена товара
    price_tag = card.find('span', {'class': 'ui-LD-ZU', 'data-testid': 'price'})
    if price_tag:
        price = price_tag.text.strip().replace('руб.', '').replace(' ', '')
        product_prices.append(int(price))

# Создание DataFrame из данных
df = pd.DataFrame({
    'Название': product_names,
    'Цена': product_prices
})

# Сохранение в CSV
df.to_csv('divan_prices.csv', index=False, encoding='utf-8-sig')

# Вывод средней цены
average_price = df['Цена'].mean()
print(f"Средняя цена диванов: {average_price} руб.")

# Построение гистограммы цен
plt.figure(figsize=(10, 6))
plt.hist(df['Цена'], bins=20, color='skyblue', edgecolor='black')
plt.title('Распределение цен на диваны')
plt.xlabel('Цена (рубли)')
plt.ylabel('Количество')
plt.grid(True)
plt.show()