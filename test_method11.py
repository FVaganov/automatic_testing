from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def test_search11():
    # инициализация драйвера
    driver = webdriver.Chrome()
    driver.maximize_window()
    # открытие страницы
    driver.get("https://memorial35.ru/")
    link_text = driver.find_element(By.CLASS_NAME, "select-city-button")
    link_text.click()
    time.sleep(10)
    # ожидание появления модального окна
    modal = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "memodal"))
    )

    # ожидание появления списка городов
    city_list = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "select-city"))
    )

    # поиск элементов списка городов
    cities = city_list.find_elements(By.CLASS_NAME, "select-city-item")

    # выбор первого города из списка
    cities[2].click()
    time.sleep(5)
    # ожидание изменения класса выбранного города
    selected_city = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "select-city-item.active"))
    )

    # проверка успешного переключения города
    if selected_city:
        print("Переключение успешно")
    else:
        print("Переключение не удалось")
    button_counter = 0
    try:
    # ожидание появления блока с id="burials"
        burials_block = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "burials"))
        )
        buttons = burials_block.find_elements(By.CLASS_NAME, "burials-list__btn")
        button_counter = len(buttons)
        print("Количество кнопок: {}".format(button_counter))
    except:
        print("Блок с кнопками не найден")

    driver.quit()
test_search11()