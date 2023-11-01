from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
def test_search16():
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
    time.sleep(5)
    # Wait for the page to load and check if login is successful
    home_button = driver.find_element(By.CSS_SELECTOR, "img[alt='search']")
    home_button.click()
    time.sleep(5)

    wait = WebDriverWait(driver, 5)
    wait.until(EC.presence_of_element_located((By.ID, "fio")))

    fio_input = driver.find_element(By.ID, "fio")
    fio_input.send_keys("Ваганов")
    fio_input.send_keys(Keys.RETURN)
    time.sleep(5)

    deads_button_1 = driver.find_element(By.CSS_SELECTOR, "img[name='deads'][id='favourites-94269']")
    deads_button_1.click()
    time.sleep(1)

    deads_button_2 = driver.find_element(By.CSS_SELECTOR, "img[name='deads'][id='favourites-28444']")
    deads_button_2.click()
    time.sleep(1)

    deads_button_3 = driver.find_element(By.CSS_SELECTOR, "img[name='deads'][id='favourites-27430']")
    deads_button_3.click()
    time.sleep(1)
    try:

        # Нажатие на катинку кнопки

        print("Добавление прошло успешно")
    except:
        print("Ошибка:добавление не удолось ")
    # Close the browser
    time.sleep(3)
    driver.quit()
test_search16()