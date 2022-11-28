<h3>В данном проекте написаны автотесты  для работы с корзиной 🛒 и поисковыми запросами 🔎 сайта  <a href="https://aliexpress.ru/">Aliexpress</a></h3>

## <h4>Описание файлов проекта:</h4>

🗔 *test_clear_carboard_product:*

**Реализованные проверки в тестах:** 

🗸 test_product_name - ```Проверка того, что товар выбраный на странице поискового запроса, соответствует товару, который открылся при его выборе, при клике на этот товар```

🗸 test_cart_five_added - ```Реализация проверки выбора пяти случайных элементов поискового запроса, на соответсвие добавленым элементам в корзину```

🗔 *conftest.py* - инициализация браузера и фикстуры, реализована проверка в разных окружениях

🗔 *BaseApp.py* - определяем базовые методы для работы с WebDriver

🗔 *PageObjects.py* - локаторы и методы 

**Реализованы методы:** 

🗸 kets_click - ```Выбор нужного элемента в поисковом запросе. Функции прокручивает страницу до нужного товара и проверяет соответствует ли товар который мы выбрали, тому который открылся в новой странице ```

🗸 add_to_card - ```Выбор пяти случайных элементов на страницах поискового запроса. Проверка, что выбраные элементы соответсвуют элементам в корзине```

**Реализована работа со *скриптами* и *парсером* <a href="https://pypi.org/project/beautifulsoup4/ ">BeautifulSoup</a>**

 - Для корректной работы кода нужно установить *LXML parser:*
 ```pip install lxml```
 
 - Либо установить его по следующему сценарию:
 ```
1. Go to File -> Settings
2. Select " Python Interpreter " on the left menu bar of settings, select "Python Interpreter."
3. Click the "+" icon over the list of packages.
4. Search for "lxml."```
5. Click "Install Package" on the bottom left of the "Available Package" window.
