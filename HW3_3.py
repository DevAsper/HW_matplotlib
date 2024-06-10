import csv
import matplotlib.pyplot as plt

def read_prices(file_path):
    prices = []

    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Пропускаем заголовок

        for row in reader:
            price = float(row[0])
            prices.append(price)

    return prices

def calculate_average(prices):
    if prices:
        return sum(prices) / len(prices)
    else:
        return None

file_path = 'cleaned_prices.csv'
prices = read_prices(file_path)
average_price = calculate_average(prices)

if average_price is not None:
    print(f'Средняя цена: {average_price:.2f} ₽')

    # Визуализация результата с помощью Matplotlib
    plt.figure(figsize=(10, 6))
    plt.hist(prices, bins=20, color='skyblue', edgecolor='black')
    plt.axvline(average_price, color='red', linestyle='dashed', linewidth=1)
    plt.text(average_price + average_price*0.05, max(plt.gca().get_ylim())*0.9, f'Средняя цена: {average_price:.2f} ₽', color = 'red')
    plt.title('Распределение цен')
    plt.xlabel('Цена (₽)')
    plt.ylabel('Количество')
    plt.show()

else:
    print('Не удалось вычислить среднюю цену. Проверьте файл на наличие корректных данных.')
