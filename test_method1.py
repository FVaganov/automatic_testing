from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_search1():
    try:
        # Создаем экземпляр драйвера Selenium (например, для Google Chrome)
        driver = webdriver.Chrome()
        driver.maximize_window()
        # Переходим на страницу, на которой производится поиск
        driver.get("https://memorial35.ru")
  
        # Вводим фамилию в поле поиска
        last_name = "Ваганов"
        search_box = driver.find_element(By.CLASS_NAME, "input-wrapper__input")
        search_box.send_keys(last_name)
        search_box.send_keys(Keys.RETURN)
        time.sleep(10)
        # Симулируем нажатие клавиши Enter для выполнения поиска
      
        
        # Ожидаем загрузки новой страницы
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "map")))

        # Проверяем результаты на новой странице
        result_element = driver.find_element(By.CLASS_NAME, "sidebar-main")
        result_text = result_element.text
    
        if last_name in result_text:
            print("Код работает: результат найден")
        else:
            print("Ошибка: результат не найден")
    except Exception as e:
        print(f"Произошла ошибка на этапе: {str(e)}")
    driver.quit()

# Запускаем тест
test_search1()