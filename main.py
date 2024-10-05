import numpy as np
import matplotlib.pyplot as plt


# Параметры нормального распределения
mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

# Построение гистограммы
plt.hist(data, bins=30, edgecolor='black', alpha=0.7)
plt.title('Гистограмма для нормального распределения')
plt.xlabel('Значения')
plt.ylabel('Частота')

# Показать график
plt.show()

# Генерация двух наборов случайных данных
x = np.random.rand(100)  # 100 случайных чисел для оси X
y = np.random.rand(100)  # 100 случайных чисел для оси Y

# Построение диаграммы рассеяния
plt.scatter(x, y, color='blue', alpha=0.6, edgecolors='black')

# Добавление заголовка и подписей осей
plt.title('Диаграмма рассеяния для случайных данных')
plt.xlabel('X значения')
plt.ylabel('Y значения')

# Показать график
plt.show()

