import pytest
from selenium import webdriver


@pytest.fixture(scope="session")  # Делаем так, чтобы браузер открывался в текущей сессиии
def browser():
    driver = webdriver.Chrome()  # Задаем браузер
    driver.set_window_size(1280, 1024)  # Делаем экран с разрешением
    yield driver  # Возвращаем генератор
    driver.quit()  # Выходим с браузера


@pytest.fixture(scope="session")  # Делаем так, чтобы браузер открывался в текущей сессиии
def browser_two():
    driver = webdriver.Chrome()  # Задаем браузер
    driver.maximize_window()  # Делаем экран с разрешением
    yield driver  # Возвращаем генератор
    driver.quit()  # Выходим с браузера