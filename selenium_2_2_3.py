import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
try:
    link = "http://suninjuly.github.io/file_input.html"
    # В переменной browser укажите путь к своему драйверу
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys("test@test.net")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test.txt')  # добавляем к этому пути имя файла
    browser.find_element(By.ID, 'file').send_keys(file_path)


    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
