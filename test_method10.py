from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_search10():
    driver = webdriver.Chrome()

    # Navigate to the login page
    driver.get("https://memorial35.ru/search?fio=%D0%B2%D0%B0%D0%B3%D0%B0%D0%BD%D0%BE%D0%B2&cemetery")
    driver.maximize_window()
    time.sleep(5)
    link_text = driver.find_element(By.CSS_SELECTOR, "a.link__text")
    link_text.click()
    time.sleep(2)
    load_elements = driver.find_elements(By.CLASS_NAME, "load")

    # Проверить наличие элементов "map__item"
    map_items = driver.find_elements(By.CLASS_NAME, "map__item")

    # Если элементы "map__item" присутствуют, удаление не удалось
    if map_items:
        print("Ошибка: Элементы с классом 'map__item' все еще присутствуют.")
    else:
        print("Удаление успешно: ")

    driver.quit()
test_search10()