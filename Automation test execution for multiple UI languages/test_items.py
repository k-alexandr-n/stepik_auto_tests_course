import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_add_to_basket_button(browser):
    """Тест: проверка наличия кнопки 'Добавить в корзину' на странице товара"""
    # URL страницы товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Ожидаем появления кнопки добавления в корзину
    try:
        add_to_basket = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket"))
        )
        print("Кнопка 'Добавить в корзину' найдена")

        # Получаем текст кнопки для проверки локализации
        button_text = add_to_basket.text
        print(f"Текст кнопки: '{button_text}' (язык: {browser.execute_script('return navigator.language')})")

        # Базовая проверка: кнопка не пустая
        assert button_text, "Кнопка 'Добавить в корзину' не содержит текста"

    except TimeoutException:
        browser.save_screenshot("error_no_add_to_basket_button.png")
        assert False, "Кнопка 'Добавить в корзину' не найдена на странице товара"

#Проверка через: pytest -s --language=es test_items.py

#pytest -s --language=en test_items.py
#pytest -s --language=es test_items.py
#pytest -s --language=fr test_items.py