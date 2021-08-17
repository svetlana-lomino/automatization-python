from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

def calc(number1, number2):
    return str((int(number1)+int(number2)))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    number1 = browser.find_element_by_css_selector("#num1")
    number1 = number1.text
    number2 = browser.find_element_by_css_selector("#num2")
    number2 = number2.text

    sum = calc(number1, number2)

    # вывод необходимого числа из visible list, открывая список №1
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(sum)

    # суммирование строк, вывод числа открывая список №2
    # browser.find_element_by_css_selector("#dropdown").click()
    # browser.find_element_by_css_selector("[value='" + sum + "']").click()

    browser.find_element_by_xpath("/html/body/div/form/button").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
