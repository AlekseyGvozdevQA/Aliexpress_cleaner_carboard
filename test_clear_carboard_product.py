from PageObject import Metods


class Test_Ali:
    def test_product_name(self, browser):
        ali_cleaner = Metods(browser)
        ali_cleaner.go_to_site()
        ali_cleaner.click_on_search_box()
        ali_cleaner.kets_click()

    def test_cart_five_added(self, browser_two):
        ali_card_add = Metods(browser_two)
        ali_card_add.go_to_site()
        ali_card_add.click_on_search_box()
        ali_card_add.add_to_card()
