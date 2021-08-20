from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element_by_css_selector('input[placeholder="Enter first name"]')
    first_name.send_keys("FirstName")
    last_name = browser.find_element_by_css_selector('input[placeholder="Enter last name"]')
    last_name.send_keys("LastName")
    email = browser.find_element_by_css_selector('input[placeholder="Enter email"]')
    email.send_keys("email@email.com")
    # получаем путь к директории текущего исполняемого скрипта lesson2_7.py
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # имя файла, который будем загружать на сайт
    file_name = "test.txt"
    # получаем путь к file_example.txt
    file_path = os.path.join(current_dir, 'test.txt')
    choose_file_button = browser.find_element_by_css_selector("#file")
    # отправляем файл
    choose_file_button.send_keys(file_path)
    button = browser.find_element_by_xpath("/html/body/div/form/button")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
