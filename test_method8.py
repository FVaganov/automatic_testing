from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def test_search8():
    # Инициализация веб-драйвера (в данном случае, Chrome)
    driver = webdriver.Chrome()
    driver.get("https://memorial35.ru")
    driver.maximize_window()
    time.sleep(2)

    try:
        # Ожидание элемента, содержащего слайдеры (предположим, это элемент с классом "about")
        wait = WebDriverWait(driver, 10)
        slider_container = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "about")))

        for _ in range(3):  # Scroll the slider three times
            # Теперь, когда блок с слайдерами доступен, выполните листание слайдов
            # Найдите слайдер внутри блока
            slider = driver.find_element(By.CSS_SELECTOR, 'img[src="/img/iphone2.f3d11bce.jpg"]')

            # Получение начальной позиции слайдера
            initial_position = slider.location['x']

            # Листание слайдера вправо
            action = ActionChains(driver)
            action.click_and_hold(slider).move_by_offset(100, 0).release().perform()
            time.sleep(2)  # Добавьте паузу для просмотра

            # Получение конечной позиции слайдера
            final_position = slider.location['x']

            # Проверка успешного листания слайдера
            if final_position > initial_position:
                print("Слайдер успешно пролистался")
            else:
                print("Ошибка при листании слайдера")
    except Exception as e:
        print(f"Ошибка: {str(e)}")
    finally:
        # Закрытие веб-драйвера
        driver.quit()
test_search8()