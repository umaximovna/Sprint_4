from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_BUTTON = By.ID, 'accordion__heading-{}'
    ANSWER_TEXT = By.ID, 'accordion__panel-{}'
    ORDER_BUTTON_IN_TOP = By.XPATH, ".//*[@class='Button_Button__ra12g']"
    ORDER_BUTTON_IN_MIDDLE = By.XPATH, ".//*[contains(@class, 'Button_Middle__1CSJM')]"
    TEXT_ON_MAIN_PAGE = By.CLASS_NAME, 'Home_Header__iJKdX'
    ACCEPT_COOKIE_BUTTON = By.XPATH, "//*[@id='rcc-confirm-button']"

