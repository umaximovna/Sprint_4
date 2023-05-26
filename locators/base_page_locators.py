from selenium.webdriver.common.by import By


class BasePageLocators:
    YANDEX_LOGO = By.XPATH, ".//*[@alt='Yandex']"
    SAMOKAT_LOGO = By.CLASS_NAME, 'Header_LogoScooter__3lsAR'
    element_from_yandex = ".//iframe[@class='dzen-search-arrow-common__frame' " \
                                    "and @aria-label='Поиск Яндекса']"

