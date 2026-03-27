from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

link = "http://suninjuly.github.io/alert_accept.html"

browser = webdriver.Edge()
browser.get(link)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)
    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(1)
    x_element = browser.find_element(By.ID, "input_value")
    x = float(x_element.text)
    y = calc(x)
    text_pole = browser.find_element(By.ID, "answer")
    text_pole.send_keys(y)
    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button1.click()

except Exception as e:
    print(f'Произошла ошибка {e}')

finally:
    time.sleep(10)
    browser.quit()