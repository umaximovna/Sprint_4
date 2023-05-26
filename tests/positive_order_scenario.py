import pytest
from selenium import webdriver
from test_data import TestData
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestPositiveOrderScenario:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @pytest.mark.parametrize('button_locator', [MainPageLocators.ORDER_BUTTON_IN_TOP,
                                                MainPageLocators.ORDER_BUTTON_IN_MIDDLE])
    @pytest.mark.parametrize('test_data', [TestData.data_for_order_1, TestData.data_for_order_2])
    def test_check_order_creation(self, button_locator, test_data):
        self.driver.get(TestData().link_of_main_page)
        main_page = MainPage(self.driver)
        main_page.accept_cookie(button_locator, test_data)
        main_page.scroll_to_element(*button_locator)
        main_page.click_order_button(*button_locator)
        order_page = OrderPage(self.driver)
        order_page.filling_basic_data_of_order(test_data.get('name'), test_data.get('last_name'),
                                               test_data.get('street'),
                                               test_data.get('station'), test_data.get('nmbr'))
        order_page.click_next_button()
        order_page.filling_rent_date(test_data.get('date'), test_data.get('index'),
                                               test_data.get('color'), test_data.get('mes'))
        order_page.click_on_button_to_order()
        order_page.click_yes()
        assert "Заказ оформлен" in order_page.check_order_is_processed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

