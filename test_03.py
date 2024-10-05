import matplotlib.pyplot as plt

x = [2, 6, 6, 6, 7, 7, 8, 10, 14]
y = [6, 4, 6, 6, 7, 7, 10, 9, 12]

plt.scatter(x, y)
plt.title('Пример диаграммы рассеивания')

plt.xlabel('Ось X')
plt.ylabel('Ось Y')

plt.show()
