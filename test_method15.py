from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def test_search15():
    # Инициализация драйвера браузера
    driver = webdriver.Chrome()
    driver.maximize_window()
    # Переход на страницу
    driver.get("https://memorial35.ru/search?fio=%D0%92%D0%90%D0%93%D0%90%D0%9D%D0%9E%D0%92&cemetery")
    time.sleep(5)
    # Нажатие на блок с id="dead-94269"
    dead_block = driver.find_element(By.ID, "dead-94269")
    dead_block.click()
    time.sleep(5)
    # Ожидание загрузки объекта с class="sidebar-main__wrapper"
    sidebar_wrapper = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "sidebar-main__wrapper"))
    )



    buttons = driver.find_elements(By.CLASS_NAME, "services-list__btn")

    for button in buttons:
        try:
            button.click()
            print("Кнопка работает")
            close_button = driver.find_element(By.CLASS_NAME, "service__close-btn")
            close_button.click()
        except:
            print("Ошибка")
    time.sleep(2)
    driver.quit()
test_search15()