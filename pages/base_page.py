from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def scroll_to_end_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_element(self, method, locator):
        element = self.driver.find_element(method, locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_any_text(self, method, locator):
        return self.driver.find_element(method, locator).text

    def click_any_button(self, method, locator):
        self.driver.find_element(method, locator).click()

