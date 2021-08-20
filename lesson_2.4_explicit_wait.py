from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

browser = webdriver.Chrome()

# browser.implicitly_wait(12)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    price_element = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element(By.XPATH, '//*[text()="$100"]')
    )
    print(price_element.text)
    book_button = browser.find_element_by_id("#book")
    book_button.click()
    print(1)

finally:
    time.sleep(30)
    browser.quit()

