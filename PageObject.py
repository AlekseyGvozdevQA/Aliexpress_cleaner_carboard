import random

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from BaseApp import BasePage
from bs4 import BeautifulSoup


class ChromeLocators:
    INPUT_SEARCH_TEXT = (By.XPATH, "//input[@id='searchInput']")
    NEEDED_CLEANER = (By.XPATH, '//div[2]/div[2]/div/div/div/div/div/div/a')
    COOKIES_BUTTOM = (By.XPATH, "//button[contains(text(),'Прекрасно')]")
    HEADING = (By.XPATH, "//h1")


class Metods(BasePage):

    def click_on_search_box(self):

        self.driverwait(ChromeLocators.COOKIES_BUTTOM).click()
        self.driverwait(ChromeLocators.INPUT_SEARCH_TEXT).clear()
        self.driverwait(ChromeLocators.INPUT_SEARCH_TEXT).send_keys('автомобильный очиститель приборной панели')
        self.driverwait(ChromeLocators.INPUT_SEARCH_TEXT).send_keys(Keys.ENTER)

    def kets_click(self):
        required_elem = []
        while not required_elem:  # до тех пор, пока не найдется нужный товар
            # составляем список всех товаров на странице
            elems = self.driver.find_elements(By.XPATH, '//div[2]/div[2]/div/div/div/div/div/div/a')
            for elem in elems:
                # проверка поискового паттерна
                if '1 шт., автомобильный бочонок мыть очиститель грязи в' in elem.text.lower():
                    required_elem.append(elem)
                    break  # досрочный выход из цикла перебора товаров, если совпадение найдено
            WebDriverWait(self.driver, 10)
            if not required_elem:  # идем дальше только если не найдено совпадение
                # функция прокручивает страницу до самого конца
                self.driver.execute_script(
                    "var scrollingElement = (document.scrollingElement || "
                    "document.body);scrollingElement.scrollTop = scrollingElement.scrollHeight;")

        for element in required_elem:
            self.driver.get(element.get_attribute("href"))
            # проверка поискового паттерна в заголовке страницы
            text = '1 шт., автомобильный бочонок мыть очиститель грязи в'
            if text in self.driver.find_element(By.XPATH, "//h1").text.lower():
                print('Страница верна')
                WebDriverWait(self.driver,
                              10)  # ожидание для того, чтобы пользователь успел просмотреть страницу с товаром
            else:
                self.driver.execute_script("window.history.go(-1)")  # возвращаемся на страницу с товарами
                print("Программе удалось найти товар в каталоге, подходящий под этот поисковый паттерн, "
                      "его страница посвящена другому товару или не удовлетворяет другим заданным требованиям.")

    def add_to_card(self):
        WebDriverWait(self.driver, 20)
        # Получаем количество найденных товаров
        products = self.driver.find_element(By.XPATH, "//div[4]/div/div/span").text
        number = []
        for i in products:
            if i.isdigit():
                number.append(i)
        len_list = int(''.join(number))
        required_elems = []
        # Составляем список 5 номеров случайных товаров
        while len(required_elems) < 5:
            num = random.randrange(1, len_list)
            if num not in required_elems:
                required_elems.append(num)
        # Ищем максимальный индекс
        max_ind = max(required_elems)
        print(max_ind)
        hrefs = []
        names = []
        while len(hrefs) < max_ind:  # до тех пор, пока не появится товар с максимальным индексом
            # составляем список всех товаров на странице
            lists = self.driver.find_elements(By.XPATH, "//div[2]/div[2]/div/div/div/div/div/div/a")
            for elem in lists:  # для каждого товара
                hrefs.append(elem.get_attribute("href"))  # получаем ссылку на товар
                # парсим название товара
                code = elem.get_attribute('innerHTML')
                soup = BeautifulSoup(code, 'lxml')
                names.append(soup.find('div').find('div').contents[0].replace('...', ''))

            if len(hrefs) < max_ind:
                # функция прокручивает страницу до самого конца
                self.driver.execute_script(
                    "var scrollingElement = (document.scrollingElement || "
                    "document.body);scrollingElement.scrollTop = scrollingElement.scrollHeight;")
        # выбираем товары с выбранными случайными индексами
        order = []
        order_names = []
        for i in required_elems:
            order.append(hrefs[i])
            order_names.append(names[i])
        i = 0
        while i < len(order):
            self.driver.get(order[i])
            if order_names[i] in self.driver.find_element(By.XPATH, "//h1").text:
                if self.driver.find_element(By.XPATH, "//button[contains(.,'В корзину')]"):
                    self.driver.find_element(By.XPATH, "//button[contains(.,'В корзину')]").click()
            else:
                print(f"Cтраница товара {order_names[i]} посвящена другому товару или не удовлетворяет другим заданным "
                      f"требованиям.")
            i += 1
        WebDriverWait(self.driver, 30)
        self.driver.find_element(By.XPATH, "//li[3]/a").click()
        WebDriverWait(self.driver, 50)