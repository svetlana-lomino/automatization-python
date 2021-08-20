from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector('input[placeholder="Input your first name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('input[placeholder="Input your last name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector('input[placeholder="Input your email"]')
    input3.send_keys("test@gmail.com")
    input4 = browser.find_element_by_css_selector('input[placeholder="Input your phone:"]')
    input4.send_keys("0999183745")
    input5 = browser.find_element_by_css_selector('input[placeholder="Input your address:"]')
    input5.send_keys("Russia")
    button = browser.find_element_by_xpath("/html/body/div/form/button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла