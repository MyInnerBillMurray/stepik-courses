from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element_by_css_selector("[name='firstname']")
    last_name = browser.find_element_by_css_selector("[name='lastname']")
    email = browser.find_element_by_css_selector("[name='email']")

    first_name.send_keys("first")
    last_name.send_keys("last")
    email.send_keys("valid@mail")

    # создаёт файл (по умолчанию в папку с текущим проектом), можно записать что-нибудь
    with open("file.txt", "w") as file:
        file.write("Nobody expects Spanish Inquisition!")
    # чтобы прикрепить файл, надо задать его путь. Он складывается из пути до текущей директории + пути до файла
    current_dir = os.getcwd()
    # или current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    # прикрепляем
    file_input = browser.find_element_by_css_selector("[name='file']")
    file_input.send_keys(file_path)
    # теперь можно удалять файл
    os.remove("file.txt")

    button = browser.find_element_by_css_selector("button")
    button.click()
    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()
