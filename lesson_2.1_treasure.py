from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    treasure_element = browser.find_element_by_css_selector("#treasure")
    treasure_valuex = treasure_element.get_attribute("valuex")
    print(treasure_valuex)

    y = calc(treasure_valuex)
    input = browser.find_element_by_xpath('//*[@id="answer"]')
    input.send_keys(y)
    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_css_selector("#robotsRule")

    # people_radio = browser.find_element_by_id("peopleRule")
    # people_checked = people_radio.get_attribute("id")
    # print(people_checked)


    button = browser.find_element_by_xpath("/html/body/div/form/div/div/button")
    button.click()



    # button = browser.find_element_by_xpath("/html/body/div/form/button")
    # button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла