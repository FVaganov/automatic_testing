from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
# Инициализация драйвера браузера, в данном случае Chrome
def test_search2():
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
    # Wait for the page to load and check if login is successful
    try:
        profile_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "sidebar-main__wrapper"))
        )
        print("Logged in successfully!")
    except:
        print("Login failed!")

    # Close the browser
    driver.quit()
test_search2()