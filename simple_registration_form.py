from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get(link)

    # говорим Selenium проверять в течение 12 секунд, пока не появится нужный нам текст $100
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    book = browser.find_element_by_css_selector("[id='book']")
    book.click()

    x = browser.find_element_by_css_selector("[id='input_value']").text
    # text возвращает текст между открывающим и закрывающим тэгом элемента, find_elementS возвращает строку
    result = str(math.log(abs(12 * math.sin(int(x)))))
    answer = browser.find_element_by_css_selector("[id='answer']")
    answer.send_keys(result)

    submit = browser.find_element_by_css_selector("[id='solve']")
    submit.click()

    # убрал time в конце, теперь он отрабатывает с кодом 0, он не успевает ловить нужный для ответа текст
    # текст этот в alert'e
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)

finally:
    browser.quit()
