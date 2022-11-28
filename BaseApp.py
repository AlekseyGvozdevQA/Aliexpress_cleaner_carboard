from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:  # В классе BasePage определяем базовые методы для работы с Драйвера

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://aliexpress.ru/"  # Указываем base_url,
        self.quantity = 0  # который будет использоваться для открытия страницы.

    def driverwait(self, locator):
        return WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(locator))

    def go_to_site(self):
        return self.driver.get(self.base_url)
    # Вызываем функцию, переходим на указанную страницу.