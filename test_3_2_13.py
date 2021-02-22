import unittest
from selenium import webdriver
import time


class Test(unittest.TestCase):

    def test1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element_by_css_selector("input[required].first")
        last_name = browser.find_element_by_css_selector("input[required].second")
        email = browser.find_element_by_css_selector("input[required].third")

        first_name.send_keys("first")
        last_name.send_keys("last")
        email.send_keys("dd@dd.com")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        browser.quit()

    def test2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element_by_css_selector("input[required].first")
        last_name = browser.find_element_by_css_selector("input[required].second")
        email = browser.find_element_by_css_selector("input[required].third")

        first_name.send_keys("first")
        last_name.send_keys("last")
        email.send_keys("dd@dd.com")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        browser.quit()


if __name__ == "__main__":
    unittest.main()
