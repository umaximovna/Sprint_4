from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_FIELD = By.XPATH, ".//*[@placeholder='* Имя']"
    LAST_NAME_FIELD = By.XPATH, ".//*[@placeholder='* Фамилия']"
    ADRESS_FIELD = By.XPATH, ".//*[@placeholder='* Адрес: куда привезти заказ']"
    NUMBER_FIELD = By.XPATH, ".//*[@placeholder='* Телефон: на него позвонит курьер']"
    STATION_FIELD = By.XPATH, ".//*[@placeholder='* Станция метро']"
    NEXT_BUTTON = By.XPATH, ".//*[text()='Далее']"

    WHEN_BRING_SCOOTER_FIELD = By.XPATH, ".//*[@placeholder='* Когда привезти самокат']"
    RENTAL_PERIOD_FIELD = By.XPATH, ".//*[@class='Dropdown-arrow']"
    RENTAL_PERIOD_MENU = By.XPATH, ".//*[@class='Dropdown-menu']/div"
    SCOOTER_COLOR_FIELD = By.XPATH, ".//*[@class='Checkbox_Label__3wxSf']"
    COMMENT_FIELD = By.XPATH, ".//*[@placeholder='Комментарий для курьера']"
    ORDER_BUTTON = By.XPATH, ".//*[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM') " \
                                "and text()='Заказать']"
    YES_OR_NO_BUTTON = By.XPATH, ".//*[contains(@class, 'Button_Button__ra12g " \
                                  "Button_Middle__1CSJM')""and text()='Нет'or text()='Да']"

    ORDER_IN_PROCESS_INFO = By.XPATH, ".//*[@class='Order_ModalHeader__3FDaJ']"
    SEE_STATUS_BUTTON = By.XPATH, "//button[text()='Посмотреть статус']"

