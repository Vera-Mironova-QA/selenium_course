from selenium import webdriver
import time
import  math

link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
browser.get(link)
def calc(x):
    return str(math.log(abs(12*math.sin(x))))
try:
    button = browser.find_element_by_css_selector('button.btn')
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(1)
    x = browser.find_element_by_id('input_value').text
    x = int(x)
    print(x)
    y = calc(x)
    input = browser.find_element_by_id('answer')
    input.send_keys(y)
    button = browser.find_element_by_tag_name("button.btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
