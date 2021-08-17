from selenium import webdriver
import time
import math

link_url1 = "https://mantle.gantri.com/products/10003/godet-table-light-by-hyeonil-jeong/10003-md-carbon"

try:
    browser = webdriver.Chrome()
    browser.get(link_url1)

    add_button = browser.find_element_by_css_selector(".add")
    add_button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# проверяем, что количество товаров равно 2
assert len(goods) == 2