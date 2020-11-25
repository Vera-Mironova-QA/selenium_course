from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/selects2.html'
browser.get(link)

try:
    a = browser.find_element_by_id('num1').text
    b = browser.find_element_by_id('num2').text
    c = str(int(a)+int(b))
    print(c)
    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(c)
    button = browser.find_element_by_css_selector('button.btn')
    button.click()
finally:
    time.sleep(10)
    browser.quit()
