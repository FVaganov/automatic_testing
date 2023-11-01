from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def test_search14():
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

    # Нажатие на кнопку с <p data-v-5df84c89="" class="map__item-cemetery block_info__dead__zoom__text"> Показать <br data-v-5df84c89="">на карте </p>
    show_on_map_button = sidebar_wrapper.find_element(By.CLASS_NAME, "block_info__dead__zoom")
    show_on_map_button.click()

    # Нажатие на class="pointer"
    pointer = driver.find_element(By.CLASS_NAME, "pointer")
    pointer.click()
    time.sleep(2)

    WebDriverWait(driver, 2).until(EC.alert_is_present())
    time.sleep(2)
                # Переключение на предупреждение и принятие его
    try:
        alert = driver.switch_to.alert
        alert.accept()
        print("Карточка работает")
    except:
        print("Ошибка")
    time.sleep(2)


    driver.quit()
test_search14()
