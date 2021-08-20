from selenium import webdriver
import time
import math

link = "http://SunInJuly.github.io/execute_script.html"
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    button = browser.find_element_by_xpath("/html/body/div/form/button")
    browser.execute_script("window.scrollBy(0, 100);")

    # или полурабочий вариант
    # browser.execute_script("arguments[0].scrollIntoView();", button)
    # time.sleep(5)

    input = browser.find_element_by_xpath("//*[@id='answer']")
    input.send_keys(y)
    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_css_selector("#robotsRule")
    option2.click()
    button.click()

finally:
    time.sleep(30)
    browser.quit()