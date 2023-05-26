import pytest
from selenium import webdriver
from test_data import TestData
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


class TestImportantQuestion:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @pytest.mark.parametrize('question_answer_number', [0, 1, 2, 3, 4, 5, 6, 7])
    def test_check_question_about_important(self, question_answer_number):
        self.driver.get(TestData().link_of_main_page)
        method_q, locator_q = MainPageLocators.QUESTION_BUTTON
        locator_q = locator_q.format(question_answer_number)
        method_a, locator_a = MainPageLocators.ANSWER_TEXT
        locator_a = locator_a.format(question_answer_number)
        MainPage.scroll_to_end_main_page(self)
        MainPage.click_question_button(self, method_q, locator_q)
        question_text = MainPage.get_any_text(self, method_q, locator_q)
        answer_text = MainPage.get_any_text(self, method_a, locator_a)
        assert answer_text == TestData().dict_of_question_answer[question_text], \
            'Ответ на вопрос не соответствует ожидаемому'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

