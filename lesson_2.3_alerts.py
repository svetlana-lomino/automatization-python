from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    iWantButton = browser.find_element_by_xpath("/html/body/form/div/div/button")
    iWantButton.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    input = browser.find_element_by_xpath('//*[@id="answer"]')
    input.send_keys(y)

    submit = browser.find_element_by_xpath("/html/body/form/div/div/button")
    submit.click()

finally:
    time.sleep(30)
    browser.quit()



