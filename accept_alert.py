import math
import time
from selenium import webdriver

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(1)
    button1 = browser.find_element_by_css_selector("[type='submit']")
    button1.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element_by_css_selector("[id='input_value']").text
    # text возвращает текст между открывающим и закрывающим тэгом элемента, find_elementS возвращает строку
    result = str(math.log(abs(12 * math.sin(int(x)))))
    answer = browser.find_element_by_css_selector("[id='answer']")
    answer.send_keys(result)

    button2 = browser.find_element_by_css_selector("button.btn")
    button2.click()
    time.sleep(1)


finally:
    time.sleep(10)
    browser.quit()
