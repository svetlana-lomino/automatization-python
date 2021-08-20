from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/wait1.html"
selector_verify_button = "#verify"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(3)
    verify_button = browser.find_element_by_css_selector(selector_verify_button)
    verify_button.click()

    message = browser.find_element_by_css_selector("#verify_message")

    assert "successful" in message.text

finally:
    time.sleep(10)
    browser.quit()


