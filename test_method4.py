from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
def test_search4():
    # Инициализация драйвера браузера, в данном случае Chrome
    driver = webdriver.Chrome()

    # Navigate to the login page
    driver.get("https://memorial35.ru")
    driver.maximize_window()
    button = driver.find_element(By.CLASS_NAME, 'account-link')
    button.click()
    # Find the phone input field by name and enter phone number
    phone_input = driver.find_element(By.NAME, "phone")
    phone_input.send_keys("9211309977")

    # Find the password input field by id and enter password
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("QDZCAE0409d")

    # Simulate pressing Enter to submit the form
    password_input.send_keys(Keys.RETURN)
    time.sleep(10)

    cards = driver.find_elements(By.CSS_SELECTOR, 'div.map__item')

    # Перебор карточек
    for card in cards:
        try:
            # Проверка наличия нужного элемента в карточке
            if card.find_elements(By.CSS_SELECTOR,'svg[data-v-77c73a79]'):
                # Находим элемент
                svg_element = card.find_element(By.CSS_SELECTOR, 'svg[data-v-77c73a79]')
                svg_element.click()

                # Нажатие на элемент клавишей Enter


                # Ожидание появления предупреждения
                WebDriverWait(driver, 5).until(EC.alert_is_present())
                time.sleep(5)
                # Переключение на предупреждение и принятие его
                alert = driver.switch_to.alert
                alert.accept()
                WebDriverWait(driver, 5).until(EC.staleness_of(card))
            print("Похоронная карточка успешно удалена.")
        except:
            print("Error encountered while processing burial card")

    # Close the browser
    driver.quit()
test_search4()