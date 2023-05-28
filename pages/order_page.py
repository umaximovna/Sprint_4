from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class OrderPage(BasePage):

    def click_logo_samokat_button(self):
        self.driver.find_element(*BasePageLocators.SAMOKAT_LOGO).click()

    def click_logo_yandex_button(self):
        self.driver.find_element(*BasePageLocators.YANDEX_LOGO).click()

    def switch_to_yandex_page(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, BasePageLocators.element_from_yandex)))

    def set_name(self, name):
        self.driver.find_element(*OrderPageLocators.NAME_FIELD).send_keys(name)

    def set_last_name(self, last_name):
        self.driver.find_element(*OrderPageLocators.LAST_NAME_FIELD).send_keys(last_name)

    def set_address(self, address):
        self.driver.find_element(*OrderPageLocators.ADRESS_FIELD).send_keys(address)

    def set_phone_number(self, phone_number):
        self.driver.find_element(*OrderPageLocators.NUMBER_FIELD).send_keys(phone_number)

    def set_metro_station(self, station):
        self.driver.find_element(*OrderPageLocators.STATION_FIELD).send_keys(station)
        self.driver.find_element(*OrderPageLocators.STATION_FIELD).send_keys(Keys.ARROW_DOWN + Keys.ENTER)

    def click_next_button(self):
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()

    def filling_basic_data_of_order(self, name, last_name, address_to_take, station, phone_number):
        self.set_name(name)
        self.set_last_name(last_name)
        self.set_address(address_to_take)
        self.set_metro_station(station)
        WebDriverWait(self.driver, 5)
        self.set_phone_number(phone_number)

    def set_when_to_bring(self, date):
        self.driver.find_element(*OrderPageLocators.WHEN_BRING_SCOOTER_FIELD).send_keys(date)

    def set_rental_period(self, index):
        self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD_FIELD).click()
        self.driver.find_elements(*OrderPageLocators.RENTAL_PERIOD_MENU)[index].click()

    def set_scooter_color(self, color_index):
        self.driver.find_elements(*OrderPageLocators.SCOOTER_COLOR_FIELD)[color_index].click()

    def set_comment_for_the_courier(self, message):
        self.driver.find_element(*OrderPageLocators.COMMENT_FIELD).send_keys(message)

    def filling_rent_date(self, date, index, color, message):
        WebDriverWait(self.driver, 5)
        self.set_when_to_bring(date)
        self.set_rental_period(index)
        self.set_scooter_color(color)
        self.set_comment_for_the_courier(message)

    def click_on_button_to_order(self):
        self.driver.find_element(*OrderPageLocators.ORDER_BUTTON).click()

    def click_yes(self):
        self.driver.find_elements(*OrderPageLocators.YES_OR_NO_BUTTON)[1].click()

    def check_order_is_processed(self):
        return self.driver.find_element(*OrderPageLocators.ORDER_IN_PROCESS_INFO).text

