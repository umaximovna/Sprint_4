from selenium.webdriver.support.wait import WebDriverWait
from test_data import TestData
from locators.main_page_locators import MainPageLocators


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def scroll_to_end_main_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_element(self, method, locator):
        element = self.driver.find_element(method, locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_any_text(self, method, locator):
        return self.driver.find_element(method, locator).text

    def click_question_button(self, method, locator):
        self.driver.find_element(method, locator).click()

    def display_main_page_text(self):
        return self.driver.find_element(*MainPageLocators.TEXT_ON_MAIN_PAGE).is_displayed()

    def accept_cookie(self, button_locator, test_data):
        WebDriverWait(self.driver, 15)
        if (button_locator == MainPageLocators.ORDER_BUTTON_IN_TOP) and (test_data == TestData.data_for_order_1):
            self.driver.find_element(*MainPageLocators.ACCEPT_COOKIE_BUTTON).click()

    def click_order_button(self, method, locator):
        self.driver.find_element(method, locator).click()

