from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os

#print(os.path.abspath(__file__)) # путь файл
#print(os.path.abspath(os.path.dirname(__file__))) # путь папка

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Edge()
browser.get(link)

current_dir = os.path.abspath(os.path.dirname(__file__))   
file_path = os.path.join(current_dir, 'file.txt')        

input1 = browser.find_element(By.NAME, "firstname")
input1.send_keys("Ivan")
input1_1 = browser.find_element(By.NAME, "lastname")
input1_1.send_keys("Petrov")
input2 = browser.find_element(By.NAME, "email")
input2.send_keys("Petrov@mail.ru")
input3 = browser.find_element(By.ID, "file")
input3.send_keys(file_path)

    # Нажимаем кнопку отправки
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
    # Ждём завершения действия (можно настроить под задачу)
time.sleep(10)
browser.quit()