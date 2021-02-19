from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("[id='input_value']")
    x = x_element.text
    # Атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента
    y = str(math.log(abs(12 * math.sin(int(x)))))
    answer = browser.find_element_by_css_selector("[id='answer']")
    answer.send_keys(y)
    checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
    checkbox.click()
    radio = browser.find_element_by_css_selector("[for='robotsRule']")
    radio.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)


finally:
    time.sleep(10)
    browser.quit()