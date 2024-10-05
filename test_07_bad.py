import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt


# Функция для парсинга цен на диваны
def parse_prices():
    url = 'https://www.divan.ru/category/divany'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Нужно уточнить класс или идентификатор, где хранятся цены
    items = soup.find_all('div', class_='LlPhw')  # нужно уточнять

    sofas = []
    for item in items:
        try:
            name = item.find('a', class_='ui-GPFV8').text.strip()
            price = item.find('span', class_='ui-LD-ZU KIkOH').text.strip().replace('₽', '').replace(' ', '')
            sofas.append([name, int(price)])
        except:
            continue

    return sofas


# Функция для сохранения данных в CSV
def save_to_csv(data, filename='sofas.csv'):
    df = pd.DataFrame(data, columns=['Название', 'Цена'])
    df.to_csv(filename, index=False, encoding='utf-8-sig')


# Функция для чтения данных из CSV и анализа
def analyze_data(filename='sofas.csv'):
    df = pd.read_csv(filename)
    print(df.head())  # Вывод первых строк для проверки

    # Средняя цена
    mean_price = df['Цена'].mean()
    print(f'Средняя цена на диваны: {mean_price:.2f} руб.')

    # Построение гистограммы
    plt.hist(df['Цена'], bins=10, edgecolor='black')
    plt.title('Гистограмма цен на диваны')
    plt.xlabel('Цена (руб.)')
    plt.ylabel('Количество')
    plt.grid(True)
    plt.show()


# Основная функция
def main():
    # Парсинг и сохранение данных
    sofas_data = parse_prices()
    save_to_csv(sofas_data)

    # Анализ данных
    analyze_data()


if __name__ == '__main__':
    main()