import math
import time
from selenium import webdriver

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(1)
    button1 = browser.find_element_by_css_selector("[type='submit']")
    button1.click()

    # лучше явно указывать окна, наверное
    # метод window_handles возвращает массив имён всех вкладок
    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_css_selector("[id='input_value']").text
    result = str(math.log(abs(12 * math.sin(int(x)))))
    answer = browser.find_element_by_css_selector("[id='answer']")
    answer.send_keys(result)

    button2 = browser.find_element_by_css_selector("button.btn")
    button2.click()
    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()
