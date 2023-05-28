from selenium import webdriver
from test_data import TestData
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestRedirectByLogo:

    def test_redirect_to_main_page_by_samokat_logo(self, driver):
        driver.get(TestData().link_of_order_page)
        order_page = OrderPage(driver)
        order_page.click_logo_samokat_button()
        main_page = MainPage(driver)
        assert driver.current_url == TestData.link_of_main_page and main_page.display_main_page_text()

    def test_redirect_to_ya_page_by_yandex_logo(self, driver):
        driver.get(TestData().link_of_order_page)
        order_page = OrderPage(driver)
        order_page.click_logo_yandex_button()
        order_page.switch_to_yandex_page()
        assert driver.current_url == TestData.link_of_yandex_page


