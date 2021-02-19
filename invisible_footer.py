from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("[id='input_value']").text
    x = str(math.log(abs(12 * math.sin(int(x_element)))))
    answer = browser.find_element_by_css_selector("[id='answer']")

    # предлагают прокручивать, но я думаю, что лучше этот футер сделать просто "прозрачным"
    footer = browser.find_element_by_tag_name("footer")
    browser.execute_script('arguments[0].style.visibility = \'hidden\'', footer)

    answer.send_keys(x)

    checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
    checkbox.click()
    radio = browser.find_element_by_css_selector("[for='robotsRule']")
    radio.click()

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
