from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

link = "https://suninjuly.github.io/execute_script.html"

browser = webdriver.Edge()
browser.get(link)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# Ожидание видимости элемента с input_value
  
x_element = browser.find_element(By.ID, "input_value")
x = float(x_element.text)
print(x, type(x))
y = calc(x)
print(y, type(y))

# Находим текстовое поле и прокручиваем к нему
text_pole = browser.find_element(By.ID, "answer")
text_pole.send_keys(y)

# Выбираем checkbox "I'm the robot"
checkbox = browser.find_element(By.ID, "robotCheckbox")
checkbox.click()

    # Переключаем radiobutton "Robots rule!"
robots_radio = browser.find_element(By.ID, "robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", robots_radio)
robots_radio.click()

    # Нажимаем кнопку отправки
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

    # Ждём завершения действия (можно настроить под задачу)
time.sleep(10)
browser.quit()