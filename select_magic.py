from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_css_selector("[id='num1']").text
    num2 = browser.find_element_by_css_selector("[id='num2']").text
    # text возвращает строку, строки складываются как строка+строка
    # select требует строку на ввод, поэтому
    # приводим два числа к int, складываем, потом приводим в строку
    the_sum = str(int(num1) + int(num2))
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(the_sum)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()
