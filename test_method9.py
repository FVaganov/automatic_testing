from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()

# Navigate to the login page
driver.get("https://memorial35.ru/search?fio=%D0%B2%D0%B0%D0%B3%D0%B0%D0%BD%D0%BE%D0%B2&cemetery")
driver.maximize_window()
time.sleep(5)
link_text = driver.find_element(By.CSS_SELECTOR, "p.link__text")
link_text.click()


date_birthday_from = driver.find_element(By.ID, "date_birthday_from")
date_birthday_from.send_keys("1920")

# Find the password input field by id and enter password
date_dead_from = driver.find_element(By.ID, "date_dead_from")
date_dead_from.send_keys("1961")

date_dead_from.send_keys(Keys.ENTER)


wait = WebDriverWait(driver, 10)
map_list = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "map__list")))

# Найти элементы "load"
load_elements = driver.find_elements(By.CLASS_NAME, "load")

# Проверить наличие элементов "map__item" внутри элементов "load"
error_flag = False
for load_element in load_elements:
    map_items = load_element.find_elements(By.CLASS_NAME, "map__item")
    if map_items:
        error_flag = True
        break

# Если элементы "map__item" присутствуют внутри элементов "load", удаление не удалось
if error_flag:
    print("Ошибка: Элементы отсутствует.")
else:
    print(" Элементы найден.")

driver.quit()