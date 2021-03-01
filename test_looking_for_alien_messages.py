import time
import math
import unittest

import pytest
from selenium import webdriver


class Test:
    message = []
    lesson_list = ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"]

    @pytest.fixture(scope="function")
    def browser(self, message=[]):
        print("\nstart browser for test..")
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        yield browser
        print("\nquit browser..")
        browser.quit()
        print(*message)

    @pytest.mark.parametrize('lesson', lesson_list)
    def test_looking_for_alien_message(self, browser, lesson, message=[]):
        link = f"https://stepik.org/lesson/{lesson}/step/1"
        browser.get(link)
        textarea = browser.find_element_by_css_selector('.textarea')
        answer = str(math.log(int(time.time())))
        textarea.send_keys(answer)
        button = browser.find_element_by_css_selector("[class='submit-submission']").click()
        text = browser.find_element_by_css_selector("[class='smart-hints__hint']").text
        if text != 'Correct!':
            message.append(text)
        assert text == 'Correct!'


if __name__ == "__main__":
    unittest.main()
