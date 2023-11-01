from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def test_search12():
    driver = webdriver.Chrome()
    driver.get("https://memorial35.ru/login")
    driver.maximize_window()


    # Найти все блоки с классом "burials-list__item swiper-slide swiper-slide-prev"
    sidebar_menu = driver.find_element(By.CLASS_NAME, "sidebar-menu")

    # Поиск катинки кнопки с нужным атрибутом alt
    home_button = sidebar_menu.find_element(By.CSS_SELECTOR, "img[alt='search']")

    # Нажатие на катинку кнопки
    home_button.click()

    sidebar_menu = driver.find_element(By.CLASS_NAME, "sidebar-menu")

    # Поиск катинки кнопки с нужным атрибутом alt
    home_button = sidebar_menu.find_element(By.CSS_SELECTOR, "img[alt='home']")

    # Нажатие на катинку кнопки
    home_button.click()
    time.sleep(2)
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "top")))
        print("Переключение на домашнюю страницу прошло успешно")
    except:
        print("Ошибка при переключении на домашнюю страницу")
    # Закрытие браузера
    driver.quit()
test_search12()