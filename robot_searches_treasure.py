from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element_by_css_selector("[id='treasure']")
    x = treasure.get_attribute('valuex')
    y = str(math.log(abs(12 * math.sin(int(x)))))
    answer = browser.find_element_by_css_selector("[id='answer']")
    answer.send_keys(y)

    checkbox = browser.find_element_by_css_selector("[id='robotCheckbox']")
    checkbox.click()
    radio = browser.find_element_by_css_selector("[id='robotsRule']")
    radio.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)


finally:
    time.sleep(10)
    browser.quit()
