import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    """Добавляем опции командной строки для выбора браузера и языка"""
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Choose browser: chrome or firefox"
        )
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Choose language code: en, es, fr, ru, etc."
        )

@pytest.fixture(scope="function")
def browser(request):
    """Фикстура для запуска браузера с указанным языком и типом браузера"""
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    if browser_name == "chrome":
        # Настройки для Chrome
        options = ChromeOptions()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': user_language}
        )
        options.add_argument(f"--lang={user_language}")
        print(f"\nЗапуск Chrome с языком: {user_language}")
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        # Настройки для Firefox
        options = FirefoxOptions()
        options.set_preference("intl.accept_languages", user_language)
        print(f"\nЗапуск Firefox с языком: {user_language}")
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError(f"Неподдерживаемый браузер: {browser_name}")

    browser.delete_all_cookies()  # Очистка кук перед тестом

    yield browser
    print("\nЗакрытие браузера..")
    browser.quit()

