import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
num_samples = 5  # Количество образцов
data_x = np.random.rand(num_samples)
data_y = np.random.rand(num_samples)

# Создание диаграммы рассеяния
plt.scatter(data_x, data_y, alpha=0.75, edgecolor='k')

# Настройка заголовка и меток осей
plt.title('Диаграмма рассеяния для двух наборов случайных данных')
plt.xlabel('Набор данных X')
plt.ylabel('Набор данных Y')

# Показ диаграммы
plt.show()
