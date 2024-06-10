from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import csv

driver = webdriver.Firefox()

# URL страницы
url = 'https://www.cian.ru/snyat-1-komnatnuyu-kvartiru/'

# Открытие страницы
driver.get(url)

# Ждем некоторое время, чтобы страница полностью загрузилась
time.sleep(5)

# Парсинг цен
prices = driver.find_elements(By.XPATH, "//span[@data-mark='MainPrice']/span")


# Открытие CSV файла
with open('prices.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

# Записываем цены в CSV файл
    for price in prices:
        writer.writerow([price.text])

# Закрытие драйвера
driver.quit()