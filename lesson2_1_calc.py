from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/math.html"
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # people_radio = browser.find_element_by_id("peopleRule")
    # people_checked = people_radio.get_attribute("checked")
    # print("value of people radio: ", people_checked)
    # assert people_checked is not None, "People radio is not selected by default"

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    input = browser.find_element_by_xpath('//*[@id="answer"]')
    input.send_keys(y)
    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_css_selector("#robotsRule")
    option2.click()

    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("id")
    print(people_checked)


    button = browser.find_element_by_xpath("/html/body/div/form/button")
    button.click()



    # button = browser.find_element_by_xpath("/html/body/div/form/button")
    # button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла