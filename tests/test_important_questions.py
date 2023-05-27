import pytest
from selenium import webdriver
from test_data import TestData
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


class TestImportantQuestion:

    @pytest.mark.parametrize('question_answer_number', [0, 1, 2, 3, 4, 5, 6, 7])
    def test_check_question_about_important(self, driver, question_answer_number):
        driver.get(TestData().link_of_main_page)
        method_q, locator_q = MainPageLocators.QUESTION_BUTTON
        locator_q = locator_q.format(question_answer_number)
        method_a, locator_a = MainPageLocators.ANSWER_TEXT
        locator_a = locator_a.format(question_answer_number)
        main_page = MainPage(driver)
        main_page.scroll_to_end_page()
        main_page.click_any_button(method_q, locator_q)
        question_text = main_page.get_any_text(method_q, locator_q)
        answer_text = main_page.get_any_text(method_a, locator_a)
        assert answer_text == TestData().dict_of_question_answer[question_text], \
            'Ответ на вопрос не соответствует ожидаемому'


