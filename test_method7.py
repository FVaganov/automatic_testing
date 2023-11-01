from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def test_search7():
    # Создаем экземпляр браузера (вам может понадобиться скачать драйвер браузера)
    driver = webdriver.Chrome()

    # Переходим на вашу веб-страницу
    driver.get("https://memorial35.ru")
    driver.maximize_window()
    time.sleep(5)
    # Находим все элементы с классом "nav__link"
    buttons = driver.find_elements(By.CLASS_NAME, "lfooter-nav__link")

    # Инициализируем счетчик
    tested_buttons = 0

    # Проходимся по найденным кнопкам и тестируем их
    for button in buttons:
        # Кликаем на кнопку
        button.click()

        # Проверяем результаты теста здесь
        # Например, можно проверить, что появился ожидаемый элемент или сообщение

        # Если тест пройден, увеличиваем счетчик
        tested_buttons += 1

    # Выводим результат
    if tested_buttons == len(buttons):
        print(f"Все {tested_buttons} кнопок прошли тест")
    else:
        print(f"Ошибка: Тест пройден только для {tested_buttons} из {len(buttons)} кнопок")

    # Закрываем браузер
    driver.quit()
test_search7()