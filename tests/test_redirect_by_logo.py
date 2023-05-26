from selenium import webdriver
from test_data import TestData
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestRedirectByLogo:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    def test_redirect_to_main_page_by_samokat_logo(self):
        self.driver.get(TestData().link_of_order_page)
        order_page = OrderPage(self.driver)
        order_page.click_logo_samokat_button()
        assert self.driver.current_url == TestData.link_of_main_page and MainPage.display_main_page_text(self)

    def test_redirect_to_ya_page_by_yandex_logo(self):
        self.driver.get(TestData().link_of_order_page)
        order_page = OrderPage(self.driver)
        order_page.click_logo_yandex_button()
        order_page.switch_to_yandex_page()
        assert self.driver.current_url == TestData.link_of_yandex_page

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

