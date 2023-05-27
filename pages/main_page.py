from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def display_main_page_text(self):
        return self.driver.find_element(*MainPageLocators.TEXT_ON_MAIN_PAGE).is_displayed()

    def accept_cookie(self):
        WebDriverWait(self.driver, 15)
        self.driver.find_element(*MainPageLocators.ACCEPT_COOKIE_BUTTON).click()


