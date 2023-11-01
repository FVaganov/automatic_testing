from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Инициализация драйвера браузера
driver = webdriver.Chrome()
driver.maximize_window()

# Переход на страницу
driver.get("https://memorial35.ru")

# Ожидание кнопок слайдера
next_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "burials-slider-button-next"))
)
prev_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "burials-slider-button-prev"))
)

# Нажатие на кнопку "next" два раза
for _ in range(2):
    next_button.click()
    time.sleep(1)

# Нажатие на кнопку "prev" два раза
for _ in range(2):
    prev_button.click()
    time.sleep(1)

# Закрытие браузера
driver.quit()