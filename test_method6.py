from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_search6():
    # Создаем экземпляр браузера (вам может понадобиться скачать драйвер браузера)
    driver = webdriver.Chrome()

    # Переходим на вашу веб-страницу
    driver.get("https://memorial35.ru/search?fio=")
    driver.maximize_window()
    time.sleep(5)

    # Находим все элементы с классом "nav__link"
    buttons = driver.find_elements(By.CLASS_NAME, "checkbox-switch")

    # Инициализируем счетчик
    tested_buttons = 0

    # Проходимся по найденным кнопкам и тестируем их
    for button in buttons:
        # Кликаем на кнопку
        button.click()

        # Ждем, пока элемент с заданным классом появится (ожидание до 10 секунд)
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "leaflet-marker-icon"))
            )
            # Если элемент появился, тест считается успешным
            print("Элемент с классом 'leaflet-marker-icon' появился")
            tested_buttons += 1
        except:
            # Если элемент не появился, тест не пройден
            print("Ошибка: Элемент с классом 'leaflet-marker-icon' не появился")

    # Выводим результат
    if tested_buttons == len(buttons):
        print(f"Все {tested_buttons} кнопок прошли тест")
    else:
        print(f"Ошибка: Тест пройден только для {tested_buttons} из {len(buttons)} кнопок")

    # Закрываем браузер
    driver.quit()

test_search6()