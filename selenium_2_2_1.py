# import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/selects1.html"
    # В переменной browser укажите путь к своему драйверу
    browser = webdriver.Chrome()
    browser.get(link)

    # x = browser.find_element(By.ID, "treasure").get_attribute("valuex")
    # y = calc(x)
    x = int(browser.find_element(By.ID, "num1").text) + int(browser.find_element(By.ID, "num2").text)
    print(x)
    Select(browser.find_element(By.TAG_NAME, "select")).select_by_value(str(x))

    # browser.find_element(By.ID, "answer").send_keys(y)
    # browser.find_element(By.ID, "robotCheckbox").click()
    # browser.find_element(By.ID, 'robotsRule').click()


    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
